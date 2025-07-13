from redhat/ubi8
workdir /root/
copy app.py  app.py
copy requirement.txt requirement.txt
copy templates/  templates/
run yum install python3 -y && pip3 install -r requirement.txt 

ENTRYPOINT ["python3" ,"app.py"]


