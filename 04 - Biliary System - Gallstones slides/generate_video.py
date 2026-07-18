#!/usr/bin/env python3
"""
Full video generation pipeline for Gallstones slides.
Steps: narrations → TTS audio → HTML→PNG → video segments → final MP4
"""

import os
import subprocess
import time

# Config
VOICE = "en-US-JennyNeural"
RATE = "-10%"
PITCH = "+5Hz"
NUM_SLIDES = 13

# Base directory
BASE = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(BASE, "slides")
NARR_DIR = os.path.join(BASE, "narrations")
AUDIO_DIR = os.path.join(BASE, "audio")
SEG_DIR = os.path.join(BASE, "segments")
PNG_DIR = os.path.join(SLIDES_DIR, "png")
OUTPUT = os.path.join(BASE, "Biliary_System_Gallstones_Kids_Video.mp4")

os.makedirs(NARR_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(SEG_DIR, exist_ok=True)
os.makedirs(PNG_DIR, exist_ok=True)


# ============================================================
# STEP 1: Write all narration scripts
# ============================================================
narrations = {
    1: """Hey there! Welcome to our adventure into the biliary system and gallstones!

Today we're going to learn all about the gallbladder and those tiny stones that can cause big trouble.

Think of your gallbladder like a small storage bag that sits right under your liver. It holds a special liquid called bile, which helps your body digest fatty foods.

Gallstones are actually the most common reason people go to the hospital for belly problems! That's a lot of people.

Ready to find out how these stones form and what we can do about them? Let's go!""",

    2: """Welcome to our table of contents!

We've got a lot to explore today. We'll start by learning what bile is made of, then look at the different types of gallstones.

We'll talk about who gets gallstones and why, what the symptoms look like, and how doctors find them.

We'll also cover how to treat gallstones and what happens when things get more serious, like cholangitis.

Stick with me — it's going to be an exciting journey!""",

    3: """Let's start with bile — the special liquid in your gallbladder!

Bile is like a recipe made of different ingredients. About 70 percent is bile salts, which help break down fats. Think of them as soap for your food!

About 22 percent is a substance called lecithin, which helps mix the oils and water together, like how dish soap mixes with water.

Only about 4 percent is cholesterol, 3 percent is protein, and a tiny 0.3 percent is bilirubin, which comes from old red blood cells.

When the balance gets thrown off — too much cholesterol or not enough bile salts — that's when trouble starts!""",

    4: """Now let's meet the three types of gallstones!

The most common type is cholesterol stones — they make up 80 out of every 100 gallstones! They form when bile has too much cholesterol and not enough bile salts.

Black pigment stones are made mostly from a substance called calcium bilirubinate. These are more common in people with blood disorders like sickle cell disease.

Brown pigment stones are the least common — less than 5 percent. They form because of infections and slow bile flow. Bacteria called E. coli and Klebsiella are often the culprits.

Even a parasite called Ascaris can cause these brown stones! Pretty wild, right?""",

    5: """Let's find out who's most at risk for getting gallstones!

There are 13 known risk factors. Being over 40 years old, being female — women have twice the risk — and using birth control pills all increase your chances.

Eating a lot of fat but not enough fiber, being overweight, and being pregnant — especially if you've had multiple pregnancies — also raise the risk.

Some medical conditions like cystic fibrosis, liver cirrhosis, and taking certain cholesterol-lowering drugs like clofibrate can contribute too.

Long periods of fasting or being on total parenteral nutrition — that's getting food through an IV — can also lead to gallstone formation.

Even something called biliary sludge, which is like thick bile, can be a risk factor!""",

    6: """Gallstones can show up in many different ways!

Some people have gallstones and don't even know it — they're completely asymptomatic. Doctors find them by accident during an ultrasound.

Chronic calculus cholecystitis means repeated episodes of biliary colic — that's the sharp belly pain from gallstones.

Acute cholecystitis is when the gallbladder gets inflamed suddenly — it's like a chemical fire that gets infected.

Other presentations include cholestasis, which is blocked bile flow, and acute cholangitis, which is a serious infection.

In rare cases, gallstones can cause pancreatitis, bowel obstruction called gallstone ileus, or even gallbladder cancer.

Remember — two thirds of gallstones are asymptomatic, but the yearly risk of developing pain is 14 percent!""",

    7: """How do doctors find gallstones? Let's look at the investigations!

Ultrasonography is the star of the show — it's the definitive test! It can see both types of stones, with 95 percent accuracy. That's really good!

An oral cholecystogram uses contrast dye to show stones as filling defects on X-ray.

A plain X-ray isn't very helpful because only 10 percent of gallstones show up on it.

MRCP is like a super-detailed MRI of the bile ducts — it's 90 percent accurate compared to ERCP.

ERCP is both diagnostic and therapeutic — doctors can find stones and remove them at the same time!

A CT scan of the abdomen gives a complete cross-sectional picture of everything going on.""",

    8: """Now let's talk about how we treat gallstone disease!

For asymptomatic gallstones — the ones found by accident — most people never develop problems. The risk of gallbladder cancer is less than one percent, which is actually lower than the risk of surgery.

But for symptomatic gallstones, things are different. There's a 12 percent chance of complications each year, and a 50 percent chance of another painful episode.

That's why treatment is recommended! The best treatment is cholecystectomy — removing the gallbladder along with the stones.

This prevents the disease from coming back because you've removed both the stones and the place where they form.

It's one of the most common surgeries done worldwide!""",

    9: """Let's zoom in on chronic calculus cholecystitis!

The main symptom is biliary colic — pain that starts in the upper right part of the belly or the epigastrium. It can travel to the area between your shoulder blades.

This pain happens when the gallbladder gets distended because a stone blocks the cystic duct. It usually lasts from 15 minutes up to 24 hours.

Doctors check for Murphy's sign — that's tenderness when they press on the right upper belly while you breathe in.

Other symptoms include nausea, vomiting, feeling full quickly, and trouble eating fatty foods.

The definitive test is ultrasound with 95 percent accuracy. Most episodes are managed at home with pain medicine and anti-nausea drugs.

If pain lasts more than 24 hours or there's a fever, it might be turning into acute cholecystitis and needs hospital care.""",

    10: """Acute cholecystitis is more serious — let's learn about it!

It starts as chemical inflammation — think of it like acid burning the gallbladder lining — then bacteria move in and make it worse.

This happens when the cystic duct stays blocked for too long.

People get mild fever, nausea, and vomiting. The pain in the right upper belly can even radiate to the right shoulder!

Complications can be scary: empyema, which is a collection of pus; gangrene, where tissue dies; fistulas, which are abnormal connections; and perforation, where the gallbladder ruptures.

Doctors use ultrasound to see a swollen, thick-walled gallbladder. Blood tests often show elevated white blood cells.

Treatment includes pain medicine, strong antibiotics given through a vein, and monitoring. Ideally, the gallbladder is removed during the same hospital stay!""",

    11: """Acute cholangitis is a medical emergency — let's learn why!

It happens when the common bile duct gets blocked and bacteria from the intestines invade. This is very serious!

Doctors look for Charcot's triad — three key symptoms together: pain in the right upper belly, yellowing of the skin called jaundice, and high swinging fever with shaking chills.

If you see all three, that's cholangitis until proven otherwise!

Treatment must start right away with broad spectrum antibiotics.

The bile duct needs to be decompressed quickly — through ERCP, which is an endoscopic procedure, or PTC, which uses a needle through the skin, or surgery if nothing else is available.

Delay can lead to septicemia — that's blood infection — or liver abscesses, both of which have high mortality rates.

Chronic cases can lead to secondary sclerosing cholangitis and biliary cirrhosis.""",

    12: """Let's learn about PTC — Percutaneous Transhepatic Cholangiography!

This is a procedure where doctors access the bile ducts through the skin and liver using a needle.

It's used for diagnosis when ERCP isn't possible — like if the patient has had stomach surgery — or when ERCP didn't work.

PTC can show the exact anatomy of the biliary tree, helping doctors plan treatment.

But it's also therapeutic! Doctors can drain infected bile, widen strictures, or place stents for cancer.

There are different drainage types: external drainage with a tube that stays for about 3 weeks, internal-external drainage that keeps pressure below 15 millimeters of mercury, and direct gallbladder drainage.

However, PTC can't be done if the patient has a bleeding disorder or severe ascites — that's fluid in the belly.""",

    13: """And that's a wrap on our gallstones adventure!

Here are the big takeaways: Gallstones are the most common abdominal reason for hospital admission. There are three main types, with cholesterol stones being the most common at 80 percent.

Ultrasound is the best test — it's 95 percent accurate. For symptomatic gallstones, removing the gallbladder is the optimal treatment.

Acute cholangitis with Charcot's triad is a medical emergency requiring urgent antibiotics and bile duct decompression.

PTC is both a diagnostic and therapeutic tool for biliary drainage.

The most important message? Don't ignore belly pain! Early treatment prevents serious complications.

Thanks for learning with me today — see you on the next adventure!"""
}


# Write all narrations
print("=== STEP 1: Writing narration scripts ===")
for i in range(1, NUM_SLIDES + 1):
    num = f"{i:02d}"
    path = os.path.join(NARR_DIR, f"narration_{num}.txt")
    with open(path, "w") as f:
        f.write(narrations[i].strip())
    wc = len(narrations[i].split())
    print(f"  narration_{num}.txt: {wc} words")

# Verify
print("\nVerification:")
for i in range(1, NUM_SLIDES + 1):
    num = f"{i:02d}"
    path = os.path.join(NARR_DIR, f"narration_{num}.txt")
    size = os.path.getsize(path)
    print(f"  {num}: {size} bytes")


# ============================================================
# STEP 2: Generate TTS Audio
# ============================================================
print("\n=== STEP 2: Generating TTS audio ===")
for i in range(1, NUM_SLIDES + 1):
    num = f"{i:02d}"
    narr_path = os.path.join(NARR_DIR, f"narration_{num}.txt")
    audio_path = os.path.join(AUDIO_DIR, f"slide_{num}.mp3")

    cmd = [
        "edge-tts",
        "--voice", VOICE,
        "--rate", RATE,
        "--pitch", PITCH,
        "-f", narr_path,
        "--write-media", audio_path
    ]
    print(f"  Generating audio for slide {num}...", end=" ", flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        # Get duration
        dur_cmd = ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", audio_path]
        dur = subprocess.check_output(dur_cmd).strip().decode()
        print(f"OK ({dur}s)")
    else:
        print(f"FAILED: {result.stderr}")


# ============================================================
# STEP 3: Convert HTML to PNG
# ============================================================
print("\n=== STEP 3: Converting HTML slides to PNG ===")
for i in range(1, NUM_SLIDES + 1):
    num = f"{i:02d}"
    html_path = os.path.join(SLIDES_DIR, f"slide-{num}.html")
    png_path = os.path.join(PNG_DIR, f"slide_{num}.png")

    cmd = [
        "google-chrome",
        "--headless=new",
        f"--screenshot={png_path}",
        "--window-size=960,540",
        f"file://{html_path}",
    ]
    print(f"  Rendering slide {num}...", end=" ", flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(png_path):
        size = os.path.getsize(png_path)
        print(f"OK ({size} bytes)")
    else:
        print(f"FAILED")
        print(f"  stderr: {result.stderr[:200]}")


# ============================================================
# STEP 4: Create video segments
# ============================================================
print("\n=== STEP 4: Creating video segments ===")
for i in range(1, NUM_SLIDES + 1):
    num = f"{i:02d}"
    png_path = os.path.join(PNG_DIR, f"slide_{num}.png")
    audio_path = os.path.join(AUDIO_DIR, f"slide_{num}.mp3")
    seg_path = os.path.join(SEG_DIR, f"slide_{num}.ts")

    if not os.path.exists(png_path) or not os.path.exists(audio_path):
        print(f"  Slide {num}: SKIPPED (missing files)")
        continue

    # Get audio duration
    dur_cmd = ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", audio_path]
    dur = subprocess.check_output(dur_cmd).strip().decode()

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", png_path,
        "-i", audio_path,
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "28",
        "-c:a", "aac", "-b:a", "128k",
        "-pix_fmt", "yuv420p", "-r", "25",
        "-t", dur, "-shortest",
        seg_path
    ]
    print(f"  Creating segment {num} (dur={dur}s)...", end=" ", flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(seg_path):
        print("OK")
    else:
        print("FAILED")
        print(f"  stderr: {result.stderr[-300:]}")


# ============================================================
# STEP 5: Concatenate segments
# ============================================================
print("\n=== STEP 5: Concatenating segments ===")
playlist_path = os.path.join(SEG_DIR, "playlist.txt")
with open(playlist_path, "w") as f:
    for i in range(1, NUM_SLIDES + 1):
        num = f"{i:02d}"
        seg_path = os.path.join(SEG_DIR, f"slide_{num}.ts")
        if os.path.exists(seg_path):
            f.write(f"file 'slide_{num}.ts'\n")

cmd = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", playlist_path,
    "-c", "copy",
    "-movflags", "+faststart",
    OUTPUT
]
print(f"  Concatenating to {os.path.basename(OUTPUT)}...", end=" ", flush=True)
result = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(OUTPUT):
    size = os.path.getsize(OUTPUT)
    print(f"OK ({size // 1024} KB)")
else:
    print("FAILED")
    print(f"  stderr: {result.stderr[-300:]}")


# ============================================================
# STEP 6: Verify & Report
# ============================================================
print("\n=== STEP 6: Final Verification ===")
if os.path.exists(OUTPUT):
    probe_cmd = [
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", "-show_streams", OUTPUT
    ]
    probe_out = subprocess.check_output(probe_cmd).decode()
    import json
    d = json.loads(probe_out)
    f = d["format"]
    dur_min = float(f["duration"]) / 60
    size_kb = int(f["size"]) // 1024
    print(f"  File: {OUTPUT}")
    print(f"  Duration: {dur_min:.1f} min")
    print(f"  Size: {size_kb} KB")
    for s in d["streams"]:
        if s["codec_type"] == "video":
            print(f"  Video: {s['width']}x{s['height']}")
        if s["codec_type"] == "audio":
            print(f"  Audio: {s['codec_name']}")
else:
    print("  ❌ Output video not found!")

print("\n✅ Video generation complete!")
