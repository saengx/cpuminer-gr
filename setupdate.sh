#!/bin/sh

apt-get update -y
apt-get upgrade -y
apt-get install libcurl4-openssl-dev -y
apt-get install libssl-dev -y
apt-get install libjansson-dev -y
apt-get install automake -y
apt-get install autotools-dev -y  
apt-get install build-essential -y
apt-get install nano -y


chmod +x edit-miner
chmod +x run-miner
chmod +x add-ip
chmod +x update
chmod +x up-grade
chmod +x ANSI_Shadow.flf
chmod +x backup
chmod +x restore
chmod +x install.txt
chmod u+x rqiner-aarch64-mobile
chmod u+x hansen33s-dero-miner-android-arm64
chmod +x edit-dero
chmod +x run-dero
chmod +x edit-qubic
chmod +x run-qubic

apt-get install python3 -y
apt-get install pip -y
apt-get install wget -y
apt-get install figlet -y
apt-get install python3-progress -y
apt-get install python3-requests -y

mv mobile-mining ../../etc
mv edit-miner ../../bin
mv run-miner ../../bin
mv edit-dero ../../bin
mv run-dero ../../bin
mv edit-qubic ../../bin
mv run-qubic ../../bin
mv add-ip ../../bin
mv update ../../bin
mv up-grade ../../bin
mv ANSI_Shadow.flf ../../usr/share/figlet
mv backup /data/data/com.termux/files/usr/bin
mv restore /data/data/com.termux/files/usr/bin
mv install.txt /storage/emulated/0/download
mv rqiner-aarch64-mobile ../../etc/mobile-mining
mv hansen33s-dero-miner-android-arm64 ../../etc/mobile-mining
mv CPUMINER ../../etc/mobile-mining
mv cpuminer-gr ../../etc/mobile-mining
cat /etc/os-release

run-miner


cd && cd ../etc/mobile-mining/ccminer
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
./build.sh

chmod +x ccminer

run-miner
