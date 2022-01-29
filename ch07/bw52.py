import subprocess

result = subprocess.run(['echo','자식 프로세스'],capture_output=True,encoding='utf-8')
result.check_returncode()
print(result.stdout)

proc = subprocess.Popen(['sleep','1'])
while proc.poll() is None:
    print('작업중...')
print('종료상태', proc.poll())

import time

start = time.time()
sleep_procs=[]
for _ in range(10):
    proc = subprocess.Popen(['sleep','1'])
    sleep_procs.append(proc)

for proc in sleep_procs:
    proc.communicate()
end = time.time()
delta = end-start
print(f'{delta:.3}초 만에 끝남')

import os
def run_encrpypt(data):
    env = os.environ.copy()
    env['password'] = 'zdfljdflajlsdffadfs'
    proc = subprocess.Popen(
        ['openssl','enc','-des3','-pass','env:password'],
        env= env,
        stdin= subprocess.PIPE,
        stdout= subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush() # ensure children's input
    return proc

procs = []
for _ in range(3):
    data =  os.urandom(10)
    proc =  run_encrpypt(data)
    procs.append(proc)

for proc in procs:
    out,_ = proc.communicate()
    print(out[-10:])