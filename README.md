# To Export Telegram Chat via Mobile App

1. Install Termux In Your Device
2. Run this code :
   ```bash
   pkg update && upgrade
   pkg install python
   pip install telethon
   ```
 
  3.Fork this Repository 

4.Get your API_ID & API_HASH from https://my.telegram.org

5. Download both Login.py & main.py and then Navigate to the folder where it was saved

6. Click on Login.py --> open with Termux --> open directory


   7.In termux type this code and hit enter 
   ```bash
   python Login.py
   ```
   8.Enter details to login
   9. Then run this code
       ```bash
       python main.py
       ```
   10. Open any chat and type !save commamd . Chat will be exported in txt file and sent to your saved msg   
   
