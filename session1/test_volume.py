import os 
assert os.path.exists("/mount"), "Use the -v or --volume flag to mount a directory or folder to /mount folder in Docker container."
print(os.listdir("/mount"))
with open("/mount/volume.txt", "w") as f:
    f.write(r"""
                |\_/|                  
                | @ @   Woof! 
                |   <>              _  
                |  _/\------____ ((| |))
                |               `--' |   
            ____|_       ___|   |___.' 
            /_/_____/____/_______|
            """)