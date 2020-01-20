# local-backup-tool
本地同步文件脚本(Locally tool for  syncing files between different media, better than the "ctrl+c &amp; ctrl +v" )
# 应用场景
将D:\YourSource备份至你的移动硬盘等介质
# Why 1
由于本人想将下载的各种文件存入移动硬盘中,ctrl+c+v 拷贝的时候,很恶心,有时我会将copy文件夹改为copy2文件夹,这样拷贝的时候系统会认为copy2是一个新的文件夹,然后复制到我的硬盘中,造成空间浪费,资源重复,除非自己手动去对比删除..
# Why 2
网上购买某些网盘,他会提供一个能使用的功能比较高级的备份工具, 但只支持他的产品, 本人不会反编及破解,故打算用Python写一个能用的就行.


# 实现方案
全量拷贝,对于已经存在的内容,做时间判断,选择最新的
对于不一致的内容的处理方案是: 
1. src有 , dest 没有 -> 复制到 dest中,
2. src没有,dest 有  -> 将dest中的删除 

# 其他的后面再慢慢更新
