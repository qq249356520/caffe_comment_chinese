#/usr/bin/env sh
DATA=examples/images
echo "Create train.txt..."
rm -rf $DATA/train.txt
#find 寻找文件
#cut 截取路径
#sed 在每行最后加上标注。本例中将找到的*cat.jpg文件加入标注为1,找到的*bike.jpg文件加入标注为2
#cat 将两个类别合并在一个文件里
find $DATA -name *cat.jpg | cut -d '/' -f3 | sed "s/$/ 1/">>$DATA/train.txt
find $DATA -name *bike.jpg | cut -d '/' -f3 | sed "s/$/ 2/">>$DATA/tmp.txt
cat $DATA/tmp.txt>>$DATA/train.txt
rm -rf $DATA/tmp.txt
echo "Done.."

