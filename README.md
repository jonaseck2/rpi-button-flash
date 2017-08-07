
```
docker run --rm --privileged \
--cap-add SYS_RAWIO \
--device /dev/mem:/dev/mem -it \
-e CHANNEL_SWITCH=17 \
-e CHANNEL_LED=18 \
-e PWM_CYCLE=0.005 \
-e NUM_FLASHES=3 \
 jonaseck/rpi-button-flash
```
