#!/usr/bin/env python3
import os, subprocess, json
VOICE="en-US-JennyNeural";RATE="-10%";PITCH="+5Hz";NUM=14
BASE=os.path.dirname(os.path.abspath(__file__))
SD=os.path.join(BASE,"slides");ND=os.path.join(BASE,"narrations")
AD=os.path.join(BASE,"audio");SG=os.path.join(BASE,"segments")
PD=os.path.join(SD,"png")
OUT=os.path.join(BASE,"Crohns_Disease_Kids_Video.mp4")
for d in [ND,AD,SG,PD]: os.makedirs(d,exist_ok=True)

narrations = {
1:"""Hey there! Welcome to our adventure into Crohn's disease!

Crohn's disease is a type of inflammatory bowel disease that can affect the entire digestive tract from your mouth all the way to the other end.

It's a chronic condition, which means it lasts a long time, and it can cause inflammation, ulcers, and even holes called fistulas in the bowel.

Today we'll learn about what causes it, who gets it, the symptoms to watch for, and the many treatments available.

There's a lot to discover — let's dive in!""",

2:"""Here's what we'll explore today!

We'll start with the genetics of Crohn's disease, including an important gene called CARD15.

Then we'll look at who gets Crohn's disease and why smoking is a big risk factor.

We'll examine how Crohn's disease damages the bowel and what symptoms it causes.

Then we'll go through all the treatment options — from lifestyle changes and medications to powerful biologic drugs and surgery.

Let's get started!""",

3:"""Let's start with the big picture of inflammatory bowel disease!

Inflammatory bowel disease, or IBD, has a complex cause. It's not just one thing — it's a combination of genetics, the immune system, and the bacteria that normally live in your gut.

In a healthy person, the immune system knows when to calm down after fighting an infection. In IBD, that calming signal doesn't work properly.

Genetics play a big role. If you have a family member with Crohn's disease, your risk is higher.

There's one gene in particular called CARD15 that's very important. People with one copy have three times the risk of developing Crohn's. People with two copies have forty times the risk!

This gene helps the immune system respond to bacteria. When it's not working right, the gut can't control inflammation properly.""",

4:"""Now let's focus on Crohn's disease specifically!

Crohn's disease is a chronic inflammatory condition that can affect any part of the digestive tract — from the mouth to the bottom. Doctors call this 'gum to bum' disease.

The inflammation goes through all layers of the bowel wall, which is why it can cause deep ulcers and holes called fistulas.

About 135,000 Canadians live with Crohn's disease. It affects about 3 to 20 people out of every 100,000 worldwide.

It usually starts before age 30, with a smaller peak around age 60. Men and women are affected equally.

Here's something interesting: smoking actually increases the risk of Crohn's disease. And when people move from Asia to Western countries, their risk goes up too.""",

5:"""Let's look at how Crohn's disease damages the bowel!

The most common location is the ileum — the last part of the small intestine — and the right side of the colon.

The inflammation creates long, linear ulcers that leave islands of normal tissue between them, creating a bumpy appearance called cobblestone mucosa.

Granulomas are tiny clumps of inflammatory cells that doctors can see under a microscope. They're found in half of all surgical specimens.

Crohn's disease is transmural, meaning it goes through all layers of the bowel. This is different from ulcerative colitis, which only affects the inner lining.

Crohn's also has skip lesions — areas of disease separated by normal bowel. And it causes deep fissures that can lead to fistulas.""",

6:"""What does Crohn's disease feel like?

The symptoms usually come and go in episodes. People get crampy abdominal pain, diarrhea that's not bloody, and weight loss.

If the ileum is inflamed, the pain happens after eating and there might be a mass in the right lower belly. It can even look like appendicitis!

Fistulas are a common problem. These are abnormal tunnels that connect the bowel to the skin, bladder, vagina, or other parts of the intestine. They can cause infections and drainage.

Perianal disease with fistulas and abscesses around the bottom is very common. Having this, being young, or needing steroids early on are signs of more aggressive disease.

Crohn's also causes problems in other parts of the body — especially the joints.""",

7:"""How do doctors diagnose Crohn's disease?

The most important test is a colonoscopy with biopsies. The doctor looks at the lining of the colon and takes small tissue samples.

CT enterography and MR enterography are special imaging tests that look at the small intestine, which a regular colonoscope can't reach.

Blood tests are also useful. C-reactive protein, or CRP, is usually elevated during active disease and helps monitor treatment response.

Doctors also check for infections that can cause similar symptoms. They test the stool for bacteria, parasites, and C. difficile.

Putting all these pieces together helps doctors make the right diagnosis and start the right treatment!""",

8:"""Let's talk about the first steps in treating Crohn's disease!

Lifestyle changes are important. The most critical one? Stop smoking! Smoking makes Crohn's disease much worse.

During a bad flare, patients may need to drink only liquids to rest the bowel. Special liquid diets called enteral diets can help achieve remission, but only for Crohn's of the ileum.

Antidiarrheal medicines like loperamide can help with symptoms. But they must be used carefully during severe flares because they can cause a dangerous complication called toxic megacolon.

Five-ASA medications like sulfasalazine and mesalamine release anti-inflammatory medicine in the bowel. They're used for mild ileitis, but their benefit in Crohn's is controversial.""",

9:"""When first treatments aren't enough, doctors turn to stronger medications!

Antibiotics like metronidazole and ciprofloxacin are especially helpful for perianal Crohn's disease. But the symptoms often come back when the antibiotics are stopped.

Corticosteroids like prednisone are very effective for acute flares. The typical dose is 40 milligrams daily. For severe disease, steroids are given through an IV.

But here's the catch — steroids don't work for maintaining remission. They should only be used for short periods to calm a flare. Long-term steroid use has many side effects.

Also, steroids can hide infections like abscesses, so doctors need to be careful. They're powerful but need to be used wisely!""",

10:"""Immunosuppressive medications help maintain remission in Crohn's disease!

The main drugs are azathioprine, 6-mercaptopurine, and methotrexate. These medicines calm the immune system to prevent flares.

They're called steroid-sparing agents because they allow patients to reduce or stop steroids without the disease coming back.

These medicines take time to work — more than 3 months in many cases. Patients usually stay on them for years.

They're often combined with biologic drugs to make the biologics work better and last longer.

Side effects can include vomiting, pancreatitis, bone marrow suppression, and a small increased risk of lymphoma.

Today, doctors are using a top-down approach — starting with stronger medications earlier rather than waiting for the disease to get worse.""",

11:"""Biologic drugs have revolutionized Crohn's disease treatment!

Infliximab, also called Remicade, is an antibody that blocks a protein called tumor necrosis factor alpha, or TNF-alpha. It's given as an IV infusion.

Adalimumab, or Humira, works the same way but is given as an injection under the skin.

Both drugs are very effective for treating fistulas and for patients who haven't responded to other treatments.

Ustekinumab is a newer biologic that blocks interleukin-12 and interleukin-23. It works through a different pathway than anti-TNF drugs.

Vedolizumab is another option that blocks a molecule called integrin, which stops inflammatory cells from traveling to the gut.

Combining a biologic with an immunosuppressant like azathioprine is more effective than using either one alone!""",

12:"""When medications aren't enough, surgery may be needed!

Surgery for Crohn's disease is usually reserved for complications. These include fistulas, bowel obstructions, abscesses, perforations, bleeding, and disease that doesn't respond to medical treatment.

During surgery, the damaged section of bowel is removed. But the disease often comes back.

Fifty percent of patients have clinical recurrence within 5 years. Eighty-five percent have recurrence within 15 years. Endoscopic recurrence is even more common.

Forty percent of patients need a second surgery, and thirty percent need a third.

One big concern is short bowel syndrome. If less than 50 percent or less than 200 centimeters of functional small intestine remains, patients can't absorb enough nutrients.""",

13:"""After ileal resection, the amount of bowel removed determines the problems that follow!

If less than 100 centimeters is removed, patients get watery diarrhea. This happens because bile salts aren't absorbed properly and end up in the colon, drawing water with them.

Treatment includes cholestyramine, which binds bile salts, or antidiarrheal medications like loperamide.

If more than 100 centimeters is removed, patients develop steatorrhea — fatty stools. This happens because there isn't enough surface area to absorb fat and not enough bile salts.

Treatment involves restricting fat in the diet and using medium-chain triglyceride supplements.

The key is that different amounts of resection need different treatments. Knowing how much bowel was removed helps guide the right therapy!""",

14:"""And that's a wrap on our Crohn's disease adventure!

Here are the big takeaways: Crohn's is a chronic transmural disease that can affect the entire GI tract.

The CARD15 gene mutation increases risk up to 40 times. Smoking makes it worse.

Symptoms include abdominal pain, diarrhea, weight loss, and fistulas.

Diagnosis uses colonoscopy with biopsy, CT or MR enterography, and blood tests.

Treatment starts with lifestyle changes and progresses through antibiotics, steroids, immunosuppressants, and biologics.

Surgery is reserved for complications, but recurrence is common — 50 percent within 5 years.

The most important message? Crohn's disease is complex, but with the right treatment team and a good plan, most people can live well!

Thanks for learning with me today — see you on the next adventure!"""
}

# STEP 1: Write narrations
print("=== STEP 1: Writing narration scripts ===")
for i in range(1,NUM+1):
    n=f"{i:02d}"
    with open(os.path.join(ND,f"narration_{n}.txt"),"w") as f: f.write(narrations[i].strip())
    print(f"  narration_{n}.txt: {len(narrations[i].split())} words")

# STEP 2: TTS Audio
print("\n=== STEP 2: Generating TTS audio ===")
for i in range(1,NUM+1):
    n=f"{i:02d}"
    subprocess.run(["edge-tts","--voice",VOICE,"--rate",RATE,"--pitch",PITCH,
        "-f",os.path.join(ND,f"narration_{n}.txt"),
        "--write-media",os.path.join(AD,f"slide_{n}.mp3")],capture_output=True,text=True)
    if os.path.exists(os.path.join(AD,f"slide_{n}.mp3")):
        d=subprocess.check_output(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",
            os.path.join(AD,f"slide_{n}.mp3")]).strip().decode()
        sz=os.path.getsize(os.path.join(AD,f"slide_{n}.mp3"))
        print(f"  slide_{n}.mp3: {sz} bytes ({d}s)")

# STEP 3: PNG
print("\n=== STEP 3: Rendering PNGs ===")
for i in range(1,NUM+1):
    n=f"{i:02d}"
    subprocess.run(["google-chrome","--headless=new",
        f"--screenshot={os.path.join(PD,f'slide_{n}.png')}","--window-size=960,540",
        f"file://{os.path.join(SD,f'slide-{n}.html')}"],capture_output=True,text=True)
    sz=os.path.getsize(os.path.join(PD,f"slide_{n}.png")) if os.path.exists(os.path.join(PD,f"slide_{n}.png")) else 0
    print(f"  slide_{n}.png: {sz} bytes")

# STEP 4: Segments
print("\n=== STEP 4: Creating video segments ===")
for i in range(1,NUM+1):
    n=f"{i:02d}"
    p=os.path.join(PD,f"slide_{n}.png");a=os.path.join(AD,f"slide_{n}.mp3");s=os.path.join(SG,f"slide_{n}.ts")
    if not os.path.exists(p) or not os.path.exists(a): print(f"  {n}: SKIPPED");continue
    dur=subprocess.check_output(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",a]).strip().decode()
    subprocess.run(["ffmpeg","-y","-loop","1","-i",p,"-i",a,"-c:v","libx264","-preset","ultrafast","-crf","28",
        "-c:a","aac","-b:a","128k","-pix_fmt","yuv420p","-r","25","-t",dur,"-shortest",s],capture_output=True,text=True)
    print(f"  segment {n}: {'OK' if os.path.exists(s) else 'FAILED'}")

# STEP 5: Concatenate
print("\n=== STEP 5: Concatenating segments ===")
with open(os.path.join(SG,"playlist.txt"),"w") as f:
    for i in range(1,NUM+1):
        n=f"{i:02d}"
        if os.path.exists(os.path.join(SG,f"slide_{n}.ts")): f.write(f"file 'slide_{n}.ts'\n")
subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",os.path.join(SG,"playlist.txt"),
    "-c","copy","-movflags","+faststart",OUT],capture_output=True,text=True)

# STEP 6: Verify
print("\n=== STEP 6: Final Verification ===")
if os.path.exists(OUT):
    p=json.loads(subprocess.check_output(["ffprobe","-v","quiet","-print_format","json","-show_format","-show_streams",OUT]))
    f=p["format"]
    print(f"  Duration: {float(f['duration'])/60:.1f} min ({float(f['duration']):.1f}s)")
    print(f"  Size: {int(f['size'])//1024} KB ({int(f['size'])//(1024*1024)} MB)")
    for s in p["streams"]:
        if s["codec_type"]=="video": print(f"  Video: {s['width']}x{s['height']}")
        if s["codec_type"]=="audio": print(f"  Audio: {s['codec_name']}")
    print("✅ Video generated!")
else: print("  ❌ Output video not found!")
