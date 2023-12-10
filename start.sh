if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SudoR2spr/Opleech-Filter-Bot.git /filterbot 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /filterbot
fi
cd /filterbot
pip3 install -U -r requirements.txt
echo "Starting Bot....."
python3 bot.py
