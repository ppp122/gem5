./build/ARM/gem5.opt configs/example/arm/fs_bigLITTLE.py \
    --caches \
    --bootloader=/data/yijia/simulator/gem5/fs_images/binaries/boot.arm64 \
    --kernel=/data/yijia/simulator/gem5/fs_images/binaries/vmlinux.arm64 \
    --disk=/data/yijia/simulator/gem5/fs_images/ubuntu-18.04-arm64-docker.img \
    --bootscript=/data/yijia/simulator/gem5/fs_images/jiajiabootscript.rcS
