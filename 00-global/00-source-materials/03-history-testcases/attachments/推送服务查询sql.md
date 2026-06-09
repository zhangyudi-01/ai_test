# 推送服务查询sql

## 明细/实时推送-sftp

#### matchup文件

```mysql
SELECT
gd.draw_time ,
s.draw_id AS DRAW_ID,
s.matchup_no AS MATCHUP_NO,
s.host_team_id AS HOST_TEAM_ID,
s.guest_team_id AS GUEST_TEAM_ID,
s.sale_end_time AS SALE_END_TIME, -- 优先使用schedule的停售时间
s.draw_flag AS DRAW_FLAG,
s.handicap AS HANDICAP, -- 来自schedule
s.matchup_desc AS MATCHUP_DESC, -- 比赛描述 (如：运动项目;单位;赛事)
NULL AS SELECTION_CNT, -- 固定空
s.sp_flag AS SP_FLAG, -- 来自schedule
s.sale_status AS MATCHUP_STATUS,-- PRD示例为2(开始销售)，对应schedule.sale_status
UNIX_TIMESTAMP(s.update_time) AS MATCHUP_TIMESTAMP, -- 转为时间戳
s.league_id AS LEAGUE_ID
FROM schedule s
left JOIN game_draw gd ON s.draw_id = gd.draw_id
WHERE
-- 明细推送-自动
 DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= DATE_SUB(CURRENT_DATE() ,INTERVAL 1 DAY) - INTERVAL 3 MONTH ;
-- 明细推送-手动
-- DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= '2025-12-20' - INTERVAL 3 MONTH ;
-- 实时推送
-- gd.draw_time >= DATE_SUB(CURRENT_DATE(), INTERVAL 14 DAY);
```

#### team文件

```mysql
-- team文件
SELECT DISTINCT
  t.team_id           AS TEAM_ID,
  NULL                AS LEAGUE_ID,     -- PRD要求固定传空
  t.team_short_name   AS TEAM_NAME,     -- PRD示例"科罗拉多急流" -> 对应 DB short_name
  t.team_name         AS TEAM_FULL_NAME,-- 对应 DB 全称
  t.is_deleted        AS DEL_FLAG,
  t.team_memo         AS TEAM_DESC,
  NULL                AS NATION_ID,     -- 固定空
  UNIX_TIMESTAMP(t.update_time) AS TEAM_TIMESTAMP
FROM team t
WHERE t.team_id IN (
    -- 查找所有符合条件的主队和客队ID
    SELECT s.host_team_id FROM schedule s
    JOIN game_draw gd ON s.draw_id = gd.draw_id
    WHERE 
	-- 明细推送-自动
	DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= DATE_SUB(CURRENT_DATE() ,INTERVAL 1 DAY) - INTERVAL 3 MONTH 
	-- 明细推送-手动
-- 	DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= '2025-12-20' - INTERVAL 3 MONTH 
	-- 实时推送
-- 	DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= (CURRENT_DATE() - INTERVAL 14 day) 
    UNION
    SELECT s.guest_team_id FROM schedule s
    JOIN game_draw gd ON s.draw_id = gd.draw_id
    WHERE 
    -- 明细推送-自动
	DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= DATE_SUB(CURRENT_DATE() ,INTERVAL 1 DAY) - INTERVAL 3 MONTH 
	-- 明细推送-手动
-- 	DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= '2025-12-20' - INTERVAL 3 MONTH 
	-- 实时推送
-- 	DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= (CURRENT_DATE() - INTERVAL 14 day) 
);
```

#### league文件

```mysql
SELECT DISTINCT
  l.league_id         AS LEAGUE_ID,
  l.league_short_name AS LEAGUE_NAME,
  l.league_name       AS LEAGUE_FULL_NAME,
  l.sport_id          AS LEAGUE_TYPE,
  '0'                 AS HIDE_FLAG,      -- 固定0
  '3'                 AS SELECTION_TYPE  -- 固定3
FROM league l
WHERE l.league_id IN (
    SELECT s.league_id FROM schedule s
    JOIN game_draw gd ON s.draw_id = gd.draw_id
    WHERE 
    -- 明细推送-自动
	DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= DATE_SUB(CURRENT_DATE() ,INTERVAL 1 DAY) - INTERVAL 3 MONTH 
	-- 明细推送-手动
-- 	DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= '2025-12-20' - INTERVAL 3 MONTH 
	-- 实时推送
-- 	DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= (CURRENT_DATE() - INTERVAL 14 day) 
);
```

#### game\_draw\_stats\_prz\_lvl文件

```mysql
SELECT
  stats.draw_id AS DRAW_ID,
  stats.draw_prz_lvl AS DRAW_PRZ_LVL,
  -- total_chances (12位)
  REPLACE(FORMAT(stats.total_chances, 12), ',', '') AS TOTAL_CHANCES,
  -- right_chances (12位)
  REPLACE(FORMAT(stats.right_chances, 12), ',', '') AS RIGHT_CHANCES,
  -- win_sp (12位)
  REPLACE(FORMAT(stats.win_sp, 12), ',', '') AS WIN_SP,
  -- win_stake_amt (4位)
  REPLACE(FORMAT(stats.win_stake_amt, 4), ',', '') AS WIN_STAKE_AMT,
  -- win_chances (12位)
  REPLACE(FORMAT(stats.win_chances, 12), ',', '') AS WIN_CHANCES,
  -- win_amt (2位)
  REPLACE(FORMAT(stats.win_amt, 2), ',', '') AS WIN_AMT,
  -- paid_chances (12位)
  REPLACE(FORMAT(stats.paid_chances, 12), ',', '') AS PAID_CHANCES,
  -- paid_amt (2位)
  REPLACE(FORMAT(stats.paid_amt, 2), ',', '') AS PAID_AMT,
  stats.withdraw_amt AS WITHDRAW_AMT,
  stats.withdrawed_amt AS WITHDRAWED_AMT,
  stats.win_selection_chances AS WIN_SELECTION_CHANCES,
  stats.paid_selection_chances AS PAID_SELECTION_CHANCES
FROM game_draw_stats_prz_lvl stats
JOIN game_draw gd ON stats.draw_id = gd.draw_id
WHERE 
  -- 自动
  DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= DATE_SUB(CURRENT_DATE() ,INTERVAL 1 DAY) - INTERVAL 3 MONTH ;
-- 手动
-- DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= '2025-12-20' - INTERVAL 3 MONTH ;
```

#### loc文件

```mysql
SELECT
	l.old_loc_id as LOC_ID,
	l.loc_name as LOC_NAME,
	l.loc_type as LOC_TYPE,
	0 as DEL_FLAG,
	r.old_rdc_id as P_LOC_ID
from loc l
left join rdc r on r.rdc_id = l.rdc_id ;


-- total_record 文件中game_draw_stats_prz_lvl 条目
SELECT
	CONCAT('game_draw_stats_prz_lvl','\t',COUNT(*))  
FROM game_draw_stats_prz_lvl stats
JOIN game_draw gd ON stats.draw_id = gd.draw_id
WHERE 
-- 自动推送
DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= DATE_SUB(CURRENT_DATE() ,INTERVAL 1 DAY) - INTERVAL 3 MONTH;
-- 手动推送
-- DATE_FORMAT(gd.draw_time,'%Y-%m-%d') >= '2025-12-20' - INTERVAL 3 MONTH;
```