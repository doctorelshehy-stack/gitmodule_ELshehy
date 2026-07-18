#!/usr/bin/env python3
"""
Video generation pipeline for Malabsorption & Coeliac Disease slides.
"""
import os, subprocess, json

VOICE = "en-US-JennyNeural"
RATE = "-10%"
PITCH = "+5Hz"
NUM_SLIDES = 15

BASE = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(BASE, "slides")
NARR_DIR = os.path.join(BASE, "narrations")
AUDIO_DIR = os.path.join(BASE, "audio")
SEG_DIR = os.path.join(BASE, "segments")
PNG_DIR = os.path.join(SLIDES_DIR, "png")
OUTPUT = os.path.join(BASE, "Malabsorption_Coeliac_Disease_Kids_Video.mp4")

for d in [NARR_DIR, AUDIO_DIR, SEG_DIR, PNG_DIR]:
    os.makedirs(d, exist_ok=True)

narrations = {
    1: """Hey there! Welcome to our adventure into malabsorption syndrome and coeliac disease!

Today we're going to learn about what happens when your body can't properly absorb nutrients from food.

Think of your small intestine like a really long absorption machine. When it doesn't work right, your body misses out on important vitamins, minerals, and nutrients.

We'll also explore coeliac disease, which is caused by eating gluten — a protein found in wheat, barley, and rye.

Ready to find out what goes wrong and how doctors fix it? Let's go!""",

    2: """Here's what we'll cover today!

We'll start with malabsorption syndrome — what it is, what causes it, and what it looks like.

Then we'll dive deep into coeliac disease, one of the most important causes of malabsorption.

We'll learn about the four different types of coeliac disease, how doctors diagnose it, and the complications to watch out for.

We'll also cover short bowel syndrome, radiation enteritis, and some rare conditions.

And we'll finish with a look at small intestine tumors. Let's get started!""",

    3: """Let's start with the big picture — what is malabsorption?

Malabsorption is when your body can't properly absorb nutrients from your food into your bloodstream.

It can be simple — affecting just one thing like fat or lactose — or complex, affecting multiple nutrients at once.

The symptoms include diarrhea, steatorrhea which means fatty stools, weight loss, and swelling called edema.

People also get belly pain and distension. Their bodies show signs of missing nutrients.

The signs doctors look for include distension, edema, and various nutritional deficiency signs. Let's learn about the causes next!""",

    4: """There are three main categories of causes for malabsorption!

First, small intestinal causes — the most common group. This includes coeliac disease, tropical sprue, bacterial overgrowth, Crohn's disease, and intestinal resection.

The small intestine is where most absorption happens, so any damage here causes big problems.

Second, pancreatic causes. The pancreas makes enzymes that help digest food. Chronic pancreatitis and pancreatic cancer can reduce these enzymes.

Third, mixed causes like Zollinger-Ellison syndrome and post-gastrectomy syndrome, where multiple systems are affected.

Each category has different treatments, so figuring out the cause is really important!""",

    5: """Malabsorption causes some important nutritional problems!

Anemia happens when you can't absorb iron, B12, or folic acid properly. Your body needs these to make red blood cells.

Edema — that's swelling — happens because of low protein in your blood. Without enough protein, fluid leaks into tissues.

Here's an interesting one: cholesterol gallstones! When bile acids aren't absorbed in the terminal ileum, bile becomes supersaturated with cholesterol, and stones form.

Osteomalacia — soft bones — happens from calcium and vitamin D malabsorption.

And vitamin A deficiency leads to night blindness. In IBD patients, joint problems affect about 20 percent, and eye problems like episcleritis occur in 3 to 4 percent.""",

    6: """How do doctors investigate malabsorption? Let's start with lab tests!

The complete blood count helps identify the type of anemia. If red blood cells are small, it's usually iron deficiency. If they're big, it's B12 or folate deficiency.

Red cell folate is a great marker for small bowel disease — it's often low in both coeliac disease and Crohn's disease.

Doctors might see Howell-Jolly bodies on the blood smear, which suggests splenic atrophy associated with coeliac disease.

Serum albumin shows nutritional status and whether protein is being lost from the gut.

Low calcium with high alkaline phosphatase suggests osteomalacia from vitamin D deficiency.

And special tests like anti-gliadin and endomysial antibodies help diagnose coeliac disease specifically!""",

    7: """Now let's look at anatomy tests and absorption tests!

For anatomy, barium meal with follow-through can show diverticula, strictures, and Crohn's disease. It's like taking an X-ray map of your intestine.

Capsule endoscopy and enteroscopy let doctors see inside directly. Biopsies of the small bowel mucosa show the microscopic damage.

CT scans look for wall thickening and abscesses, while MRI enteroclysis avoids radiation entirely.

For absorption tests, the stool fat collection is important — normally less than 6 grams per day. The D-xylose test checks if the proximal intestine is absorbing properly.

The lactose tolerance test diagnoses lactase deficiency. And hydrogen breath tests detect bacterial overgrowth.

These tests help doctors pinpoint exactly where the problem is!""",

    8: """Now let's talk about coeliac disease — a very important condition!

Coeliac disease is when the upper small bowel lining gets inflamed because of gluten — a protein in wheat, barley, and rye.

About 1 percent of people have it, but many don't even know! Here's how it works:

Gliadin peptides from gluten slip through the gut lining because the tight junctions are compromised. Then tissue transglutaminase — that's an enzyme — makes them even more inflammatory.

These modified peptides activate CD4 T cells through special markers called HLA-DQ2 or DQ8.

The T cells release interferon-gamma and other chemicals that damage the intestinal villi — those are the tiny finger-like projections that absorb nutrients.

This whole cascade leads to villous atrophy and the symptoms of coeliac disease!""",

    9: """Coeliac disease has four different clinical subtypes!

Typical coeliac disease starts between 6 and 24 months when babies start eating gluten. Kids get poor growth, abnormal stools, belly distension, muscle wasting, and seem unhappy.

Atypical coeliac disease is seen in older kids and adults. They don't have obvious malabsorption but may have belly pain, dental enamel defects, mouth ulcers, or even raised liver enzymes.

Silent coeliac disease hides in people with family history or autoimmune conditions like Type 1 diabetes. They might have irritability, poor school performance, chronic fatigue, and iron deficiency anemia.

Latent or potential coeliac disease has normal-looking intestine but positive antibodies. It's associated with Down syndrome, Turner syndrome, and Type 1 diabetes.

All four types respond to a gluten-free diet!""",

    10: """Diagnosing coeliac disease involves several steps!

First, specific blood antibodies: tissue transglutaminase IgA, endomysial IgA, and anti-gliadin IgA. These are the three main tests.

Important note: if someone is IgA deficient — which can happen — doctors should check for tTG IgG instead.

If antibodies stay elevated after 12 months on a gluten-free diet, it usually means the patient isn't following the diet properly.

In 6 to 9 percent of cases, especially in elderly or immunocompromised patients, coeliac disease can be seronegative — meaning antibodies are negative.

HLA genetic testing for DQ2 and DQ8 is very useful — if you don't have these markers, you almost certainly don't have coeliac disease.

The gold standard is upper endoscopy with at least 6 duodenal biopsies showing villous atrophy — worse in the proximal duodenum!""",

    11: """Let's talk about complications and treatment of coeliac disease!

Complications include enteropathy-associated T-cell lymphoma — a serious cancer that can develop. There's also ulcerative jejunitis with fever, pain, and bleeding.

Small bowel adenocarcinoma risk is increased, and dermatitis herpetiformis — a blistering skin condition — is linked to gluten sensitivity.

The good news? Malignancy risk is reduced by following a gluten-free diet!

For treatment, the key is avoiding gluten. That means no wheat, rye, barley, or couscous.

Safe foods include rice, maize, buckwheat, potato, and many others. Oats are now considered safe if uncontaminated.

All natural foods like vegetables, fruits, meat, fish, eggs, and milk are fine. And supplements help with any remaining iron, calcium, or vitamin deficiencies.

The crossed ear of wheat symbol identifies certified gluten-free products!""",

    12: """Exciting new treatments for coeliac disease are being developed!

Researchers are working on several approaches based on understanding the disease mechanism.

Fontolizumab is a humanized antibody against interferon-gamma that shows promise.

Infliximab is used for severe, life-threatening refractory cases. Alemtuzumab helps patients at risk for lymphoma.

Interleukin-10 can suppress the T cell activation that causes damage.

Beyond these drugs, scientists are engineering gluten-free grains that taste like regular ones.

Exogenous endopeptidases — special enzymes — can break down gliadin peptides before they cause harm.

Zonulin receptor blockers and transglutaminase inhibitors can reduce gut permeability.

HLA-DQ2 antagonists and oral tolerance induction to gluten are other exciting approaches.

These could eventually allow coeliac patients to eat gluten safely!""",

    13: """Let's learn about short bowel syndrome and radiation enteritis!

Short bowel syndrome happens when more than 1 meter of small intestine is removed. The jejunum is better tolerated than the ileum because that's where bile salts and B12 are absorbed.

After ileal resection, bile salts enter the colon causing diarrhea. If more than a third of bile salts are lost, fat digestion fails and gallstones form.

Oxalate absorption increases in the colon, leading to kidney stones. B12 deficiency is common.

Radiation enteritis occurs when radiation therapy exceeds 40 gray. The ileum and rectum are most affected since pelvic radiation is common for gynecological and urinary cancers.

Acute symptoms improve within 6 weeks. But chronic radiation enteritis — lasting more than 3 months — affects over 15 percent of patients and causes obstruction from fibrotic strictures.

Treatment is mainly symptomatic, and surgery should be avoided whenever possible!""",

    14: """Let's finish with other causes and small intestine tumors!

Giardia parasites can cause both diarrhea and steatorrhea. Cryptosporidiosis is especially problematic in HIV patients.

Eosinophilic gastroenteritis is linked to asthma and eczema, treated with steroids.

Intestinal lymphangiectasia causes protein loss with ankle swelling. Low-fat diet helps.

Now, small intestine tumors are rare — only 3 to 6 percent of GI tumors. The fluidity and rapid transit of intestinal contents provide protection.

Adenocarcinoma is the most common type, usually in the duodenum. Lymphomas are found in the ileum.

Carcinoid tumors make up 10 percent of small bowel neoplasms. Only 5 percent develop carcinoid syndrome with liver metastases — causing flushing, diarrhea, and heart valve problems.

Treatment uses octreotide and lanreotide. Peutz-Jeghers syndrome causes pigmented spots and polyps throughout the GI tract!""",

    15: """And that's a wrap on malabsorption and coeliac disease!

Here are the big takeaways: Malabsorption is when your body can't absorb nutrients properly. There are three categories of causes.

Coeliac disease affects 1 percent of people and has four clinical subtypes. Diagnosis uses antibodies and biopsy.

The gluten-free diet is the cornerstone of treatment — avoiding wheat, rye, and barley while enjoying rice, maize, and many other foods.

Complications like lymphoma are reduced by sticking to the diet. New immunotherapies offer hope for the future.

Short bowel syndrome and radiation enteritis are important causes of malabsorption too.

The most important message? If you have chronic diarrhea, weight loss, or nutrient deficiencies — get checked! Early diagnosis and treatment make a huge difference.

Thanks for learning with me today — see you on the next adventure!"""
}


# STEP 1: Write narrations
print("=== STEP 1: Writing narration scripts ===")
for i in range(1, NUM_SLIDES + 1):
    num = f"{i:02d}"
    path = os.path.join(NARR_DIR, f"narration_{num}.txt")
    with open(path, "w") as f:
        f.write(narrations[i].strip())
    wc = len(narrations[i].split())
    print(f"  narration_{num}.txt: {wc} words")


# STEP 2: Generate TTS Audio
print("\n=== STEP 2: Generating TTS audio ===")
for i in range(1, NUM_SLIDES + 1):
    num = f"{i:02d}"
    narr_path = os.path.join(NARR_DIR, f"narration_{num}.txt")
    audio_path = os.path.join(AUDIO_DIR, f"slide_{num}.mp3")
    cmd = ["edge-tts", "--voice", VOICE, "--rate", RATE, "--pitch", PITCH,
           "-f", narr_path, "--write-media", audio_path]
    print(f"  Slide {num}...", end=" ", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(audio_path):
        dur = subprocess.check_output(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",audio_path]).strip().decode()
        print(f"OK ({dur}s)")
    else:
        print(f"FAILED: {r.stderr[:100]}")


# STEP 3: Convert HTML to PNG
print("\n=== STEP 3: Converting HTML to PNG ===")
for i in range(1, NUM_SLIDES + 1):
    num = f"{i:02d}"
    html = os.path.join(SLIDES_DIR, f"slide-{num}.html")
    png = os.path.join(PNG_DIR, f"slide_{num}.png")
    subprocess.run(["google-chrome","--headless=new",f"--screenshot={png}","--window-size=960,540",f"file://{html}"],
                   capture_output=True, text=True)
    print(f"  Slide {num}: {'OK' if os.path.exists(png) else 'FAILED'} ({os.path.getsize(png) if os.path.exists(png) else 0} bytes)")


# STEP 4: Create video segments
print("\n=== STEP 4: Creating video segments ===")
for i in range(1, NUM_SLIDES + 1):
    num = f"{i:02d}"
    png = os.path.join(PNG_DIR, f"slide_{num}.png")
    audio = os.path.join(AUDIO_DIR, f"slide_{num}.mp3")
    seg = os.path.join(SEG_DIR, f"slide_{num}.ts")
    if not os.path.exists(png) or not os.path.exists(audio):
        print(f"  {num}: SKIPPED"); continue
    dur = subprocess.check_output(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",audio]).strip().decode()
    subprocess.run(["ffmpeg","-y","-loop","1","-i",png,"-i",audio,
                    "-c:v","libx264","-preset","ultrafast","-crf","28",
                    "-c:a","aac","-b:a","128k","-pix_fmt","yuv420p","-r","25",
                    "-t",dur,"-shortest",seg], capture_output=True, text=True)
    print(f"  Segment {num}: {'OK' if os.path.exists(seg) else 'FAILED'}")


# STEP 5: Concatenate
print("\n=== STEP 5: Concatenating segments ===")
playlist = os.path.join(SEG_DIR, "playlist.txt")
with open(playlist, "w") as f:
    for i in range(1, NUM_SLIDES + 1):
        num = f"{i:02d}"
        if os.path.exists(os.path.join(SEG_DIR, f"slide_{num}.ts")):
            f.write(f"file 'slide_{num}.ts'\n")

subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",playlist,
                "-c","copy","-movflags","+faststart",OUTPUT], capture_output=True, text=True)


# STEP 6: Verify
print("\n=== STEP 6: Final Verification ===")
if os.path.exists(OUTPUT):
    probe = json.loads(subprocess.check_output(["ffprobe","-v","quiet","-print_format","json","-show_format","-show_streams",OUTPUT]))
    f = probe["format"]
    print(f"  File: {OUTPUT}")
    print(f"  Duration: {float(f['duration'])/60:.1f} min ({float(f['duration']):.1f}s)")
    print(f"  Size: {int(f['size'])//1024} KB ({int(f['size'])//(1024*1024)} MB)")
    for s in probe["streams"]:
        if s["codec_type"] == "video": print(f"  Video: {s['width']}x{s['height']}")
        if s["codec_type"] == "audio": print(f"  Audio: {s['codec_name']}")
else:
    print("  ❌ Output video not found!")

print("\n✅ Done!")
