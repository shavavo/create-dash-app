import os, shutil, glob, subprocess

name, ssh, port = input("Application name (subdomain): "), input("SSH Endpoint (ie. [NET_ID]@netvisdev.fuqua.duke.edu): "), input("Port: ")
project_dir, deploy_dir = '../{}-DEV/'.format(name), '../{}-DEPLOY/'.format(name)

shutil.copytree('package/DEV/', project_dir, symlinks=False, ignore=None)
shutil.copytree('package/DEPLOY/', deploy_dir, symlinks=False, ignore=None)

for directory in [project_dir, deploy_dir]:
    for filename in glob.iglob(directory + '**/*.sh', recursive=True):
        generator_dir, generated_name = os.path.dirname(filename), filename.split('_')[-1][0:-3]
        subprocess.call(['bash {} > {}/{} {} {} {}'.format(filename, generator_dir, generated_name, name, port, ssh)], shell=True)
        os.remove(filename)

print('')
print('Created project at ' + project_dir)
print('Syncing for the first time..')

subprocess.call(['bash sync.sh > logs.txt'], cwd=project_dir, shell=True)

url = ssh.split('@')[-1]
print('')
print('{} now deployed at https://{}/{}'.format(name, url, name))
print('To run locally in development environment, run "python main.py" in {}-DEV/main/app'.format(name))

