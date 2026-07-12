echo "BUILD START"
python3.14 -m pip install -r requirements.txt
python3.14 manage.py collectstatic --noinput --clear
echo "BUILD END"