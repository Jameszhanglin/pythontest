

  /********************************
文件列表 FS_File_Manager_List 86,0,'30031'
--liji 20150317 文件索引放在批发库，在同步到zb库
--liji 20160304 图片名称没有时用fileno加.jpg替代
--songyl 20170517 正京元查看批发上传的商品电子资料加user
********************************/
ALTER   PROCEDURE dbo.LSFS_File_Manager_List
 @UserID     int,
    @FileType   INT = 0,
    @FileKeyID  varchar(50),
    @BusiType INT = 0
AS
 set nocount on

--if @busitype = 1 or exists (select * from TBR_FILETYPE WHERE Filetype = @FileType and RelationType = 1)
-- begin
--  if exists(select * from dbo.sysobjects where name='user_FS_File_Manager_List' and type='P')
--  BEGIN
--   EXEC user_FS_File_Manager_List
--   @UserID     ,
--   @FileType   ,
--   @FileKeyID  ,
--   @BusiType

--   RETURN
--  END
-- end


if @busitype = 4
 begin
  if exists(select * from dbo.sysobjects where name='user_FS_File_Manager_List' and type='P')
  BEGIN
   EXEC user_FS_File_Manager_List
   @UserID     ,
   @FileType   ,
   @FileKeyID  ,
   @BusiType

   RETURN
  END
 end

-- if @busitype = 2 or exists (select * from TBR_FILETYPE WHERE Filetype = @FileType and RelationType = 2)
-- begin
--  if exists(select * from dbo.sysobjects where name='user_FS_File_Manager_List2' and type='P')
--  BEGIN
--   EXEC user_FS_File_Manager_List2
--   @UserID     ,
--   @FileType   ,
--   @FileKeyID  ,
--   @BusiType

--   RETURN
--  END
-- end

    declare @sql nvarchar(2000)
    declare @datebase varchar(100)
 select @datebase = DbLink from TBR_FILETYPE WHERE Filetype = @FileType
--
    declare @webdatebase varchar(100)
    --select @webdatebase=paravalue from systempara where paraid=1000012

    --SET @webdatebase='zbfile'

    set @sql=N'
    select a.filetype,a.filekeyid,a.fileno,
    case when a.filename='''' then convert(varchar,a.fileno)+''.jpg'' else a.filename end as filename,
    a.opuser,case when a.filename='''' then convert(varchar,a.fileno)+''.jpg'' else a.filename end as oldfile,
    b.typename as FileTypeName from [zbpfdb].zbpf7.dbo.zskFILEKEY_bl a inner join [zbpfdb].zbpf7.dbo.TBR_FILETYPE b on a.Filetype = b.Filetype
    inner join TR_matecode c on a.商品id=c.jxkk_pfgid
    where c.gid=@FileKeyID and (a.Filetype =@FileType or @FileType = 0)
    --and (b.relationtype = @BusiType or @BusiType=0)
    order by b.filetype,a.fileno'
    print @sql
     exec sp_executesql    @sql,
     N'
     @FileType int,
     @FileKeyID varchar(20),
     @BusiType int
     ',
     @FileKeyID=@FileKeyID,
     @FileType=@FileType,
     @BusiType=@BusiType