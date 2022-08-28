if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SadKidBGMZ/fwdbot.git /fedbot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone https://github.com/SadKidBGMZ/fwdbot
fi
ls
cd SadKidBGMZ/fwdbot
ls
$PWD
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
