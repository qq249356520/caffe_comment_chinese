#!/usr/bin/env sh
set -e
 
snap_dir="examples/mytest_scale/snapshots"
 
mkdir -p $snap_dir
 
TOOLS=./build/tools
 
 
$TOOLS/caffe train --solver=examples/mytest_scale/mysolver.prototxt 2>&1 | tee -a $snap_dir/train.log
