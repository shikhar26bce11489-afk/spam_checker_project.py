import re 

def detect_spam(spamnotification ):
    spamnotification = spamnotification.lower().strip()
    score = 0
    reason = []

    # Checkpoints and their risk points according to their dangerousness/seriousness
    checkpoints = {
        "Urgent language": {
            "patterns" : [r"urgent", r"immediately", r"within 24 hours", r"last chance"],
            "risk points": 65
        },
        "Money related message": {
            "patterns":[r"send money",r"transfer", r"pay now", r"gift card", r"deposit", r"crypto", r"account details", r"wallet"],
            "risk points": 80
        },
        "Fake Authority": {
            "patterns": [r"bank", r"police", r"income tax", r"customs" , r"courier", r"amazon", r"flipkart", r"cyber cell", r"microsoft"],
            "risk points" : 70
        },
        "Asking personal info": {
            "patterns" : [r"otp",r"password",r"pin",r"cvv", r"account number", r"ifsc", r"adhaar",r"pan"],
            "risk points"   : 90
        },   
        "Suspicious links" : {
            "patterns": [r"http[s]?://", r"bit\.ly", r"tinyurl", r"goo.gl", r"check below"],
            "risk points" : 60
        }
    }

    # Now check all checkpoints and give risk points
    for category, data in checkpoints.items():   
        for pattern in data["patterns"]:
            if re.search(pattern,spamnotification):  
                score += data["risk points"]
                reason.append(category)
                break      #count each category only once

    # Final score limit
    score = min(score, 100)

    #result
    print("\n" + "="*45)
    print(f"Risk Score : {score}/100")


    if score >= 75:
        print("Status : HIGH RISK (LIKELY SCAM/SCAM)")
              
    elif score >= 40 :
        print("Status : MEDIUM RISK (BE CAREFUL)")

    else : 
        print("Status : LOW RISK(LOOKS SAFE)") 

    if reason :
        print("REASON  :", ", ".join(set(reason)))
    else:
        print("Reason  : No strong spam signals found")
    print("="*45)


# main program
print ("===== Local Spam / Scam Message Checker ====")
print ("Paste the message below (press Enter twice to check ):\n")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

spamnotification = " ".join(lines)

if spamnotification.strip():
    detect_spam(spamnotification)
else:
    print("No message entered ")    

    
        