#!/usr/bin/env python3
"""Video generation pipeline for Small Intestine Diseases slides."""
import os, subprocess, json

VOICE = "en-US-JennyNeural"
RATE = "-10%"
PITCH = "+5Hz"
NUM_SLIDES = 14
BASE = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(BASE,"slides")
NARR_DIR = os.path.join(BASE,"narrations")
AUDIO_DIR = os.path.join(BASE,"audio")
SEG_DIR = os.path.join(BASE,"segments")
PNG_DIR = os.path.join(SLIDES_DIR,"png")
OUTPUT = os.path.join(BASE,"Small_Intestine_Diseases_Kids_Video.mp4")
for d in [NARR_DIR,AUDIO_DIR,SEG_DIR,PNG_DIR]: os.makedirs(d,exist_ok=True)

narrations = {
1: """Hey there and welcome to our adventure into small intestine diseases!

Your small intestine is a long, winding tube where most of your food gets digested and absorbed. When things go wrong here, it can cause all sorts of problems.

Today we'll learn about short bowel syndrome, which happens when part of the intestine is removed. We'll explore radiation enteritis, parasitic infections, and some rare conditions.

We'll also discover tumors of the small intestine, carcinoid syndrome, and a special condition called Peutz-Jeghers syndrome.

There's so much to learn — let's dive in!""",

2: """Here's what we'll explore today!

We'll start with short bowel syndrome — what happens after intestinal resection and the metabolic problems that follow.

Then we'll look at radiation enteritis, which affects people who've had radiation therapy for cancer.

We'll also cover parasitic infestations like Giardia, and protein-losing enteropathy.

Then we'll dive into some rarer conditions like eosinophilic gastroenteritis, intestinal lymphangiectasia, and abetalipoproteinaemia.

Finally, we'll learn about small intestine tumors, carcinoid tumors, and Peutz-Jeghers syndrome.

Let's get started!""",

3: """Let's start with short bowel syndrome!

This happens when more than 1 meter of the small intestine has been surgically removed. The jejunum handles removal better than the ileum because that's where bile salts and B12 are absorbed.

After ileal resection, several problems occur. First, bile salts enter the colon and cause diarrhea — this is called bile-salt induced diarrhea.

Second, when too many bile salts are lost, fat can't be digested properly, leading to fatty stools and gallstones.

Third, the colon absorbs more oxalate, which can lead to kidney stones.

Fourth, vitamin B12 deficiency develops because the ileum is where B12 is absorbed.

The good news? The intestine can adapt over time — it takes about a year!""",

4: """Now let's talk about radiation enteritis!

Radiation therapy above 40 gray can damage the intestine. The ileum and rectum are most affected because pelvic radiation is common for treating gynecological and urinary cancers.

In the acute phase, patients experience nausea, vomiting, diarrhea, and abdominal pain. These symptoms usually improve within 6 weeks after treatment ends.

But chronic radiation enteritis is diagnosed when symptoms last more than 3 months. It affects over 15 percent of patients.

The main problem is abdominal pain from obstruction caused by fibrotic strictures — scar tissue that narrows the bowel.

Treatment is mostly supportive, and surgery should be avoided if possible. It's only used for obstruction or perforation.

Acute radiation proctitis with diarrhea and bleeding can sometimes be helped with local steroid treatment.""",

5: """Let's look at parasitic infestations and protein-losing enteropathy!

Giardia intestinalis is a parasite that causes both diarrhea and malabsorption with fatty stools. The organism can be found in the jejunal fluid or the intestinal lining.

Cryptosporidiosis is another parasitic infection that causes malabsorption. It's especially dangerous for patients with HIV.

Protein-losing enteropathy is a condition where the intestine loses protein into the gut. This leads to low albumin levels in the blood, which causes swelling in the feet and legs.

Usually, it's part of a larger disorder, but sometimes the liver can't make enough albumin to keep up with the losses.

The key is to treat whatever is causing the underlying problem!""",

6: """Let's learn about amyloidosis and rheumatic disorders!

Amyloidosis is a condition where abnormal protein deposits build up in tissues throughout the body, including the gastrointestinal tract.

When the small intestine is involved, the main symptom is diarrhea. The deposits can also appear as polyp-like growths.

Systemic sclerosis, also known as scleroderma, most commonly affects the esophagus, but can also involve the small bowel and colon.

When it does, reduced motility leads to bacterial overgrowth, which causes diarrhea and fatty stools.

In rheumatoid arthritis and lupus, gastrointestinal symptoms can occur but rarely dominate the clinical picture.

Each of these conditions requires treating the underlying disease to improve the gut symptoms.""",

7: """Now let's explore eosinophilic gastroenteritis!

This is a rare condition where eosinophils — a type of white blood cell — build up in the lining of the stomach and small intestine.

We don't know exactly what causes it, but it's linked to allergies like asthma, eczema, and hives.

The symptoms include abdominal pain, nausea, vomiting, and even upper GI bleeding. The gastric antrum and proximal small intestine are most commonly involved.

Interestingly, only 20 percent of patients have high eosinophil levels in their blood. That means normal blood work doesn't rule it out!

Diagnosis is made by taking a biopsy during endoscopy, which shows the eosinophilic infiltration in the tissue.

Treatment is with steroids, especially when there's widespread involvement.""",

8: """Let's learn about intestinal lymphangiectasia!

This condition involves dilation of the lymphatic vessels in the intestine. It can be primary or secondary to problems like malignancy or constrictive pericarditis.

When the lymphatics are dilated, lymph fluid leaks into the intestine. This causes loss of proteins, leading to low albumin levels and ankle swelling — that's the main symptom.

Immunoglobulins and lymphocytes are also lost, so patients have weakened immune systems.

Treatment starts with a low-fat diet, which reduces lymph flow. Fat-soluble vitamin supplements are also important.

In some primary cases, octreotide can have a dramatic effect by reducing lymphatic leakage.

The key is to identify and treat any underlying cause for secondary cases!""",

9: """Abetalipoproteinaemia is a very rare genetic disorder!

It's caused by a failure to make special proteins called apolipoproteins that are needed to transport fats. Without these, the body can't form chylomicrons, which are packages that carry fats from food.

This leads to fat accumulation in the intestinal cells, giving a characteristic appearance on biopsy.

The clinical features include acanthocytosis — that's red blood cells with spiky projections due to abnormal membranes.

Patients also develop retinitis pigmentosa, which causes vision loss.

And there are serious neurological problems that affect movement and thinking.

But here's the good news: vitamin E injections can prevent the neurological damage from getting worse.

It's a great example of how understanding a disease mechanism leads to effective treatment!""",

10: """Let's explore small intestine tumors!

The small intestine is surprisingly resistant to cancer. Only 3 to 6 percent of all gastrointestinal tumors occur here, and less than 1 percent of all cancers.

This protection comes from several factors: the liquid contents flow through quickly, the environment is relatively sterile, and there's lots of immune tissue that produces protective IgA antibodies.

Risk factors for small intestine cancer include coeliac disease, Crohn's disease, Peutz-Jeghers syndrome, and familial adenomatous polyposis.

So while tumors are rare in this part of the body, certain people are at higher risk and need regular monitoring.

Let's look at the specific tumor types next!""",

11: """Let's learn about the different types of small intestine tumors!

Adenocarcinoma is the most common type. It's found most frequently in the duodenum, especially near the ampulla of Vater, and in the jejunum.

Lymphomas are most often found in the ileum. In developed countries, the most common type is B-cell lymphoma arising from mucosa-associated lymphoid tissue, or MALT.

T-cell lymphomas look different — they form ulcerated plaques or strictures in the proximal small bowel.

There's also a special type similar to Burkitt's lymphoma that affects the terminal ileum of children in North Africa and the Middle East.

Other tumors include lipomas, stromal tumors, adenomas, and polyps from familial adenomatous polyposis that can progress to adenocarcinoma.

Each type requires different treatment approaches!""",

12: """Now let's talk about carcinoid tumors, which are really fascinating!

Carcinoid tumors come from special cells called enterochromaffin cells that produce hormones. They make up about 10 percent of all small bowel tumors.

The most common locations are the appendix, terminal ileum, and rectum. Ten percent of appendix carcinoids present as acute appendicitis.

Most carcinoids don't cause symptoms and are found when they've already spread to the liver.

Carcinoid syndrome happens in only 5 percent of patients, and only when there are liver metastases. It causes bluish-red flushing of the face and neck, watery diarrhea, abdominal pain, and heart valve problems.

The tumors secrete serotonin, bradykinin, and other active substances that cause these symptoms.

Diagnosis is made by measuring urine levels of 5-HIAA, which is a breakdown product of serotonin.

Treatment uses octreotide and lanreotide — these drugs control symptoms and sometimes slow tumor growth. Most patients survive 5 to 10 years after diagnosis!""",

13: """Let's finish with Peutz-Jeghers syndrome!

This is an inherited condition with two main features: dark spots on the skin and polyps in the digestive tract.

The pigmentation is most common around the mouth — 95 percent of patients have it — but also appears on the hands and feet. The brown spots inside the cheeks are characteristic of this condition.

The polyps are hamartomas, which are benign growths, and they can appear anywhere in the GI tract but are most common in the small bowel.

Half of patients develop intussusception, where the bowel telescopes into itself, causing obstruction.

Treatment involves removing polyps with endoscopy. Bowel surgery is avoided if possible, but may be needed for gangrenous bowel.

Regular yearly checks with endoscopy are essential because there's a high risk of cancer developing over time.

Early detection and surveillance make all the difference!""",

14: """And that's a wrap on our small intestine diseases adventure!

Here are the big takeaways: Short bowel syndrome after massive resection causes bile-salt diarrhea, steatorrhea, oxalate stones, and B12 deficiency.

Radiation enteritis from over 40 gray causes acute symptoms that improve within 6 weeks, but chronic cases affect more than 15 percent of patients.

Parasitic infections like Giardia and cryptosporidiosis can cause serious malabsorption, especially in immunocompromised patients.

Rare conditions like intestinal lymphangiectasia and abetalipoproteinaemia require specific dietary treatments.

Small intestine tumors are surprisingly rare — only 3 to 6 percent of all GI tumors.

Carcinoid tumors cause flushing, diarrhea, and heart problems through hormone secretion. Treatment with octreotide is effective.

Peutz-Jeghers syndrome needs regular surveillance because of high cancer risk.

The most important message? The small intestine may be small, but it's mighty important for your health!

Thanks for learning with me today — see you on the next adventure!"""
}

# STEP 1: Write narrations
print("=== STEP 1: Writing narration scripts ===")
for i in range(1,NUM_SLIDES+1):
    num = f"{i:02d}"
    with open(os.path.join(NARR_DIR,f"narration_{num}.txt"),"w") as f:
        f.write(narrations[i].strip())
    print(f"  narration_{num}.txt: {len(narrations[i].split())} words")

# STEP 2: TTS Audio
print("\n=== STEP 2: Generating TTS audio ===")
for i in range(1,NUM_SLIDES+1):
    num = f"{i:02d}"
    r = subprocess.run(["edge-tts","--voice",VOICE,"--rate",RATE,"--pitch",PITCH,
        "-f",os.path.join(NARR_DIR,f"narration_{num}.txt"),
        "--write-media",os.path.join(AUDIO_DIR,f"slide_{num}.mp3")],capture_output=True,text=True)
    if os.path.exists(os.path.join(AUDIO_DIR,f"slide_{num}.mp3")):
        d = subprocess.check_output(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",
            os.path.join(AUDIO_DIR,f"slide_{num}.mp3")]).strip().decode()
        print(f"  slide_{num}.mp3 OK ({d}s)")
    else:
        print(f"  slide_{num}.mp3 FAILED: {r.stderr[:100]}")

# STEP 3: HTML to PNG
print("\n=== STEP 3: Converting HTML to PNG ===")
for i in range(1,NUM_SLIDES+1):
    num = f"{i:02d}"
    subprocess.run(["google-chrome","--headless=new",
        f"--screenshot={os.path.join(PNG_DIR,f'slide_{num}.png')}",
        "--window-size=960,540",
        f"file://{os.path.join(SLIDES_DIR,f'slide-{num}.html')}"],capture_output=True,text=True)
    sz = os.path.getsize(os.path.join(PNG_DIR,f"slide_{num}.png")) if os.path.exists(os.path.join(PNG_DIR,f"slide_{num}.png")) else 0
    print(f"  slide_{num}.png: {sz} bytes")

# STEP 4: Video segments
print("\n=== STEP 4: Creating video segments ===")
for i in range(1,NUM_SLIDES+1):
    num = f"{i:02d}"
    p = os.path.join(PNG_DIR,f"slide_{num}.png")
    a = os.path.join(AUDIO_DIR,f"slide_{num}.mp3")
    s = os.path.join(SEG_DIR,f"slide_{num}.ts")
    if not os.path.exists(p) or not os.path.exists(a): print(f"  {num}: SKIPPED"); continue
    dur = subprocess.check_output(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",a]).strip().decode()
    subprocess.run(["ffmpeg","-y","-loop","1","-i",p,"-i",a,"-c:v","libx264","-preset","ultrafast","-crf","28",
        "-c:a","aac","-b:a","128k","-pix_fmt","yuv420p","-r","25","-t",dur,"-shortest",s],capture_output=True,text=True)
    print(f"  segment {num}: {'OK' if os.path.exists(s) else 'FAILED'}")

# STEP 5: Concatenate
print("\n=== STEP 5: Concatenating segments ===")
with open(os.path.join(SEG_DIR,"playlist.txt"),"w") as f:
    for i in range(1,NUM_SLIDES+1):
        num = f"{i:02d}"
        if os.path.exists(os.path.join(SEG_DIR,f"slide_{num}.ts")):
            f.write(f"file 'slide_{num}.ts'\n")
subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",os.path.join(SEG_DIR,"playlist.txt"),
    "-c","copy","-movflags","+faststart",OUTPUT],capture_output=True,text=True)

# STEP 6: Verify
print("\n=== STEP 6: Final Verification ===")
if os.path.exists(OUTPUT):
    p = json.loads(subprocess.check_output(["ffprobe","-v","quiet","-print_format","json","-show_format","-show_streams",OUTPUT]))
    f = p["format"]
    print(f"  Duration: {float(f['duration'])/60:.1f} min ({float(f['duration']):.1f}s)")
    print(f"  Size: {int(f['size'])//1024} KB ({int(f['size'])//(1024*1024)} MB)")
    for s in p["streams"]:
        if s["codec_type"]=="video": print(f"  Video: {s['width']}x{s['height']}")
        if s["codec_type"]=="audio": print(f"  Audio: {s['codec_name']}")
    print("✅ Video generated successfully!")
else:
    print("  ❌ Output video not found!")
