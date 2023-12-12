if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SudoR2spr/Opleech-Filter-Bot.git /Opleech-Filter-Bot 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Opleech-Filter-Bot
fi
cd /Opleech-Filter-Bot 
pip3 install -U -r requirements.txt
echo "Starting Opleech-Filter-Bot 😎...."
python3 bot.py    
