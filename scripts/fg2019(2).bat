cd "C:\Program Files\FlightGear 2019.2.0(2)\bin\"

#fgfs.exe --enable-fullscreen --aircraft=c172p --airport=KJYO --runway=35 --timeofday=noon --prop:/sim/model/hide-yoke=true --multiplay=out,10,mpserver51.flightgear.org,5000

#fgfs.exe --enable-fullscreen --aircraft=c172p --airport=KJYO --runway=35 --timeofday=noon --prop:/sim/model/hide-yoke=true --multiplay=out,10,mpserver51.flightgear.org,5000 --native-fdm=socket,out,30,192.168.254.127,5500,udp --generic=socket,out,10,255.255.255.255,49002,udp,foreflight-xatt

fgfs.exe --enable-fullscreen --aircraft=c172p --airport=KJYO --runway=35 --timeofday=noon --prop:/sim/model/hide-yoke=true --multiplay=out,10,mpserver51.flightgear.org,5000 --generic=socket,out,1,255.255.255.255,49002,udp,foreflight-xatt --generic=socket,out,1,192.168.254.109,49002,udp,foreflight-xgps