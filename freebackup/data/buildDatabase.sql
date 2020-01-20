DROP table  if exists t_backup_b4;
drop table if exists t_backup_end;
drop table if exists bak_history;

create table t_backup_b4(
  id integer  primary key autoincrement,
  stable_dir  text,
  dynamic_dir text,
  stable_modtime text,
  dynamic_modtime text
);
--
create table bak_history(
    id integer primary key autoincrement,
    bak_time text
);
--
