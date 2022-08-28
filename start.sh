echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/hockbhmv/fwdbot /fwdbot 
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/hockbhmv/fwdbot -b $BRANCH /fwdbot
fi
cd /fwdbot 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
