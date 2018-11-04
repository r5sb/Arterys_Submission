###############################################################
#Submission Code for Arterys Machine Learning Intern Position.#
# One of the most unique applications I've ever submitted :D  #
# - Sidharth Makhija                                          #
###############################################################
 
 #Usage: python3 submission_script.py --resume 'Resume.pdf' --cover 'Cover.pdf' --code 'submission_script.py'
 
import urllib.request  
import json
import subprocess
import pdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--resume", type = str, help="Enter resume filename as pdf!")
parser.add_argument("--cover", type = str, help="Enter cover letter filename as pdf!")
parser.add_argument("--code", type = str, help="Enter code file as .py !")
args = parser.parse_args()

def get_md5(file_name):
	temp =  subprocess.Popen("md5sum " + file_name, shell=True, stdout=subprocess.PIPE).stdout
	temp2 =  temp.read()
	md5 = temp2.decode().split(' ')[0]
	return md5

def get_base64(file_name):
	temp =  subprocess.Popen("base64 " + file_name, shell=True, stdout=subprocess.PIPE).stdout
	temp2 =  temp.read()
	base = temp2.decode()
	return base

resume_md5 = get_md5(args.resume)
cover_md5 = get_md5(args.cover)
code_md5 = get_md5(args.code)

resume_base64 = get_base64(args.resume)
cover_base64 = get_base64(args.cover)
code_base64 = get_base64(args.code)

json_body = {
    "email": "ssm9575@rit.edu",
    "name": "Sidharth Makhija",
    "position": "Machine Learning Intern",
    "notes": "github.com/r5sb",
    "phone": "(585) 755-4004",
    "documents": {
        "resume": {
        "content": resume_base64,
        "md5": resume_md5
        },
        "cover_letter": {
        "content": cover_base64,
        "md5": cover_md5
        },
        "code": {
        "content": code_base64,
        "md5": code_md5,
        "filename": "Sidharth_Makhija_Arterys_Submission_Code.py"
        }
    },
    "test_or_submit": "submit"
}

submission_url = "secret-link"
http_req = urllib.request.Request(submission_url)
http_req.add_header('Content-Type', 'application/json; charset=utf-8')
json_data = json.dumps(json_body)
json_bytes = json_data.encode('utf-8')
http_req.add_header('Content-Length', len(json_bytes))
pls_hire_me = urllib.request.urlopen(http_req, json_bytes)
