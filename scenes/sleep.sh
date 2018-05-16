curl http://localhost:3000/sound/stop
curl http://localhost:3000/switch/2/on
echo "Sleep my boy"
echo "Nice music"
curl http://localhost:3000/sound/sleep &
echo "Switch on blanket"
curl http://localhost:3000/switch/1/on 
echo "A little light at first"
curl http://localhost:3000/dim/2/100
echo "Make it comfortable"
curl http://localhost:3000/angle/A/0
sleep 4
curl http://localhost:3000/angle/B/0
echo "No light"
curl http://localhost:3000/dim/2/90
sleep 4
curl http://localhost:3000/switch/2/off
