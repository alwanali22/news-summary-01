import os
import sys

SUMMARY = '''World news, Wednesday 11 November 2026

Russia and Ukraine ended two days of US-mediated talks in Abu Dhabi agreeing a major prisoner exchange — the biggest of the war, numbers due Thursday — but no ceasefire or territorial deal (Reuters). Zelenskyy called it "constructive and quite substantive"; US envoys Kushner and Witkoff head to Moscow to meet Putin.

In the US-Iran war, Marco Rubio said in Paris the US economic campaign was devastating enough that "no major combat operations" were needed (New York Times). Iran's security chief Mohsen Rezaei said Tehran awaited a US reply to seven conditions for talks, the Strait of Hormuz shut and no enriched uranium leaving Iran. US prosecutors charged three Iran-backed operatives over about 20 plots, including one at RAF Fairford.

At COP31 in Antalya, UN chief António Guterres told 102 world leaders the slow climate response had put the world "on a path to destruction" and urged a fossil-fuel tax (AFP). Australia, Bangladesh, Kenya, Nigeria and Vanuatu backed doubling solar roofs by 2030.

Israel swore in a parliament with no government after a deadlocked election; its forces killed at least seven in Gaza, including a father and his 13-year-old son, health officials said. The House voted 211-204 to kill an impeachment bid against Defense Secretary Hegseth.

Four million Spaniards struck over housing for the first time in 14 years, unions said (CNN). Russia's US ambassador Alexander Darchiev died suddenly in Moscow aged 66 (Reuters). Congo's Ebola outbreak passed 11,000 cases, 5,387 deaths (Reuters); Kenya discharged its last patient.

US stocks rallied: the S&P 500 rose 1.3% to 7,619, the Nasdaq 1.6% as CoreWeave jumped 25% (AP). Brent topped $92; gold fell below $4,000.

Also: Yemen said it hit Houthi positions in six provinces, claiming about 190 fighters killed or injured; hoax bomb threats hit thousands of schools in Italy and Britain; a US soldier was arrested in Britain on suspicion of spying for Russia.'''

def main():
    """Writes the news summary to the specified output directory."""
    if not (1 <= len(SUMMARY) <= 2000):
        sys.stderr.write("Error: SUMMARY is not between 1 and 2000 characters long\n")
        sys.exit(1)
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, "entry.txt")
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        f.write(SUMMARY)

if __name__ == "__main__":
    main()
