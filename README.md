# checksumcrawler

App take as an argument a file or a directory. 

When you specify only file name, md5 checksum of the file will be returned. This usage is useless in my opinion because you can use linux tool md5sum, i.e. md5sum filename.iso.

Checksum crawler starts to show it strengths when you have a directory of files that you want to copy and you dont want to copy file one by one and calculate checksum for all of them but copy whole directory and calculate checksums automatically for all files. 

In this sceanrio app will genareat output file which you can copy to second computer and run the app in  compare mode.

How to use:
1. git clone project

2. go to directory where checker.py is located

3. run command:
python3 checker.py /home/tom/downloads --output md5s.txt

4. file md5s.txt will be created

5. copy file to next pc.

6. run command 
python3 checker.py /home/tom/downloads --compare md5s.txt

7. If comparing end with sucess you will see OK in console. If not app will print to the console files that were copied not corectly.
