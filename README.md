# checksumcrawler

App take as an argument a file or a directory. 

When you specify only file name, md5 checksum of the file will be returned. This usage is useless in my opinion because you can use linux tool md5sum, i.e. md5sum filename.iso.

Checksum crawler starts to show it strengths when you have a directory of files that you want to copy and you don't want to copy files one by one and calculate checksum for all of them but copy whole directory and calculate checksums automatically for all the files. 

In this sceanrio app will genareat output file which you can copy to second computer and run the app in  compare mode.

How to use:
1. git clone project

2. go to directory where checker.py is located

3. run command:
python3 checker.py /home/tom/downloads
Full path to directory needs to be specified.

4. file sums.txt will be created

5. copy sums.txt file to location where files where copied.

6. run command 
python3 checker.py /home/tom/downloads --compare sums.txt

7. If comparing end with sucess you will see OK in console. If not app will print to the console files that were copied not corectly and creates file errors.txt.


App also calculates if number of files in both directories is the same. So you can chek if all files were coppied.

Size of files in directories doesn't matter to this program, because it reads them in buffers. One restriction is that output data is stored in file, then during the comparison mode this entire file is loaded into memory, so if you have humongous number of files it can be a problem. Solving that is unnecessary for my purposes. PR that solves this is much appriciated. 
