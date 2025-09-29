# speech_analysis.py
# UN Speech Sentiment Analysis - VSCode Version

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re
import os

# Download NLTK data (will only download once)
def setup_nltk():
    """Download required NLTK data"""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    
    # Download other required datasets
    nltk_downloads = ['punkt_tab', 'averaged_perceptron_tagger', 'brown', 'wordnet']
    for dataset in nltk_downloads:
        try:
            nltk.download(dataset, quiet=True)
        except:
            pass

print("Setting up NLTK...")
setup_nltk()
print("NLTK setup complete!")

# ============================
# 1. DEFINE THE SPEECHES
# ============================

shettima_speech = """
This is the speech delivered by Nigeria's Vice President Kashim Shettima at the 80th session of the United Nations General Assembly on Wednesday, 24th September.

Madam President, Mr. Secretary-General, Excellencies, Heads of State and Government, Distinguished Delegates, the chaos that shadows our world is a reminder that we cannot afford the luxury of inaction. We would have been consumed by our differences had there been no community such as this to remind us that we are one human family. Even in our darkest hours, we have refused to be broken. This community was born from the ashes of despair, a vehicle for order and for the shared assurance that we could not afford to falter again.

Our belief in this community is not a posture of moral superiority but an undying faith in the redemption of humanity. It is, therefore, with profound humility that I stand before you today as Vice President of the Federal Republic of Nigeria, on behalf of President Bola Ametenebu, to renew this pledge on behalf of my country.

Madam President, Nigeria joins the Committee of Nations in congratulating you on your election as President of the General Assembly for the 88th session, and I assure you of our unalloyed support during your tenure. I commend your predecessor, my brother, His Excellency Philemon Young, and the Secretary-General, His Excellency Antonio Guterres, for their outstanding stewardship and unifying leadership during these extraordinary times.

This anniversary will not be a sentimental retreat into nostalgia. It must be a moment of truth, a pause to measure where we have stumbled and how we might have done better in turning our values into action that meets the demands of today. We are here to deliver a world of peace and development, while the respect for human rights is paramount.

We must recalibrate the delicate balance between our roles as sovereign governments and our duties as collective partners to renew multilateralism in a world that has evolved far beyond what it was in 1945. The face of change across borders is a force without pause. It manifests in the tools of technology, in the movements of information and finance, in the corrosive ideologies that preach violence and division, in the gathering storm of the climate emergency, and in the tide of irregular migration. We must own this process of change.

When we speak of nuclear disarmament, the proliferation of small weapons, Security Council reform, peer access to trade and finance, and the conflicts and human suffering across the world, we must recognise the truth: this stands on our collective humanity. For all our careful diplomatic language, the slow pace of progress on these hardy perennials of the UN General Assembly debate has led some to look away from the multilateral model.

Some years ago, I noticed a shift at this gathering. Key events were beginning to take place outside this hall, and the most sought-after voices were no longer heads of state. These are indeed troubling times. Nigeria remains firmly convinced of the merits of multilateralism. But to sustain that conviction, we must show that existing structures are not set in stone. We must make real change, change that works, and change that is seen to work. If we fail, the direction of travel is already predictable.

We are here to strengthen the prospect for peace, development, and human rights. Madam President, I want to make four points today to outline how we can do this. One, Nigeria must have a permanent seat at the UN Security Council. This should take place as part of a wider process of institutional reform. Two, we need urgent action to promote sovereign debt relief and access to trade and financing. Three, countries that host minerals must benefit from those minerals. And fourth, the digital divide must close. As our Presidential Secretary-General has said, AI must stand for Africa Included.

On my first point, the United Nations will recover its relevance only when it reflects the world as it is, not as it was. Nigeria's journey tells this story with clarity. When the UN was founded, we were a colony of 20 million people, absent from the tables where decisions about our fate were taken. Today, we are a sovereign nation of 236 million people, projected to be the third most populous country in the world, with one of the youngest and most dynamic populations on Earth, a stabilising force in regional security, and a consistent partner in global peacemaking.

Our case for a permanent seat at the Security Council is a demand for fairness, for representation, and for reform that restores credibility to the very institution upon which the hope of multilateralism rests. This is why Nigeria stands firmly behind the UN80 initiative of the UN Secretary-General and the resolution adopted by this Assembly on 18th July 2025, a bold step to reform the wider United Nations system for greater relevance, efficiency, and effectiveness in the face of unprecedented financial strain.

We support the drive to rationalise structures and end the duplication of responsibilities and programmes so that this institution may speak with one voice and act with greater coherence. Madam President, none of us in this world can function peacefully in isolation. This is a heavy burden of sovereignty. Sovereignty is a covenant of shared responsibility, a recognition that our survival is bound to the survival of others.

To live up to this charge, we must work hand in hand with our neighbours and partners. We must follow the trails of weapons, of money, and of people. For these forces, too often driven by pestilence, non-state actors ignite the fires of conflict across our region.

Madam President, Nigeria's soldiers and civilians carry a proud legacy. They have participated in 51 out of 60 United Nations peacekeeping operations since our independence in 1960. We have stood with our partners in Africa to resolve conflicts, and we continue that commitment today through the Multinational Joint Task Force.

At home, we confront this culture of insurgency we resolve from this long and difficult struggle with violent extremism. One truth stands clear. Military tactics may win battles measured in months and years, but in wars that span generations, it is values and ideas that deliver the ultimate victory.

We are despised by terrorists because we choose tolerance over tyranny. Their ambition is to divide us and to poison our humanity with a toxic rhetoric of hate. Our difference is the distance between shadow and light, between despair and hope, between the ruin of anarchy and the promise of order. We do not only fight wars. We pity and shelter the innocent victims of war.

This is why we are not indifferent to the devastations of our neighbours near and distant. This is why we speak of the violence and aggression visited upon innocent civilians in Gaza, the illegal attack on Qatar, and the tensions that scarred the wider region. It is not only because of the culture of impunity that makes such acts intolerable, but because our own bitter experience has taught us that such violence never ends where it begins.

We do not believe that the sanctity of human life should be trapped in the corridors of endless debate. That is why we say, without stuttering and without doubt, that a two-state solution remains the most dignified path to lasting peace for the people of Palestine. For too long, this community has borne the weight of moral conflict. For too long, we have been caught in the crossfire of violence that opened the conscience of humanity.

We come not as partisans, but as peacemakers. We come as brothers and sisters of a shared world, a world that must never reduce the right to live into the currency of devious politics. The people of Palestine are not collateral damage in a civilisation searching for order. They are human beings, equal in worth, entitled to the same freedoms and dignities that the rest of us take for granted.

We want to make the choice crystal clear: civilised values over fear, civilised values over vengeance, civilised values over bloodshed. We show the opportunities that peace brings, just as the extremists hope to drive apart rival communities and different religions. We work through multilateral platforms within the rule of law to build the consensus and support that makes this immensely difficult and dangerous task that much easier.

It is our experience that this offers the best path, the only hope for peace, reconciliation, and victory for the civilised values of a shared humanity. Nigeria is a diverse country. It also recognises the variable geometry of democracy in different forms and speeds. For this reason, we are working with the United Nations to strengthen democratic institutions in our region and beyond through the regional partnership for democracy.

Madam President, point two. The price of peace is eternal vigilance. The increasingly difficult security outlook has prompted many members to count the cost of the emerging world order. We in Nigeria are already familiar with such difficult choices: infrastructure renewal or defence platforms, schools or tanks. Our view is that the path to sustainable peace lies in growth and prosperity.

The government has taken difficult but necessary steps to restructure our economy and remove distortions, including subsidies and currency controls that benefited the few at the expense of the many. I believe in the power of the market to transform. Our task is to enable and facilitate and to trust in the ingenuity and enterprise of the people. But the process of transition is difficult and brings unavoidable hardship.

This year, we held the inaugural West African Economic Summit in Abuja to bring investors and opportunities together. The results far exceeded our expectations and are a clear indication of what innovation can deliver. It is in that same spirit of dynamic review that I invite the United Nations to examine the best use of scarce resources.

One critical area is climate change. It is not an abstract issue about an indeterminate path to be settled at some distant point in the future. It is not even solely an environmental issue. It is about national, regional, and international security. It is about irregular migration. Truly, this is an everyone issue. We are all stakeholders and we are all beneficiaries of the best outcomes.

Madam President, this is why relevant ministers have been instructed to work with the UN to make the best use of climate funds. We believe there are huge shared dividends to accrue from increased support for education, for resilient housing, for access to technology and financing to allow vulnerable communities to thrive, to become part of solutions rather than problems. Nigeria and Africa have made significant strides in recent years to put our affairs in order.

We can take that progress to the next level, a level that presents new opportunities for trade, investment, and profit if we can access reforms to strengthen the international financial architecture. We need urgent action to promote debt relief, not as an act of charity, but as a clear path to the peace and prosperity that benefits us all. I am calling for new unbinding mechanisms to manage sovereign debt, a sort of international court of justice for money that will allow emerging economies to escape the economic straitjacket of primary production of unprocessed exports.

It has been over four decades since the Lagos Plan of Action outlined a route away from debt and dependence that highlighted opportunities that today should still be explored for local added value for processing and manufacturing in everything from agriculture to solid minerals and petrochemicals. The African Continental Free Trade Area is a remarkable achievement of cooperation. We remain fully committed to the achievement of the SDGs and are convinced that this can be best delivered by focusing principally on our primary mission of growth and prosperity.

Madam President, on our third point, we welcome steps to move towards peace in the Democratic Republic of Congo. We agree that international investment and engagement offer a way out of the cycle of decay and violence. Access to strategic minerals from Sierra Leone in the 1990s and Sudan today has for too long been a source of conflict rather than prosperity.

Africa, and I must include Nigeria, has in abundance the critical minerals that will drive the technologies of the future. Investments in exploration, development and processing of these minerals in Africa will diversify supply to the international market, reduce tensions between major economies and help shape the architecture for peace and prosperity on a continent that too often in the past has been left behind by the rivalries and competition between different power blocs.

We know in Nigeria that we are more stable when those communities that have access to key resources are able to benefit from these resources. This has been our journey in the oil-producing region of the Niger Delta. I believe that will strengthen the international order when those countries that produce strategic minerals benefit purely from those minerals in terms of investment, partnership, local processing and jobs. When we export raw materials as we have been doing, tension, inequality and instability fester.

Madam President, the fourth pillar for change that I am advocating is a dedicated initiative, bringing together researchers, private sector, government and communities to close the digital divide. As we stand on the threshold of new and dramatic technological change, we are still absorbing the impact of the revolution on information and communication of the past 20 years. We understand better than we did the opportunities technology offers as well as the safeguards we need to enable growth and mitigate the potential for corrosion.

Some worry about fake news. Truly, we have plenty of that with the potential of devastating real-world consequences in countries rich and poor. I am more worried about an emerging generation that grows even more cynical because it believes nothing and trusts less.

As technology shakes up public administration, law, finance, conflict and so much of the human condition, I am calling for a new dialogue to ensure we promote the best of the opportunities that are arising and promote the level of access that allows emerging economies more quickly to close a wealth and knowledge gap that is in no one's interest.

I join you today to reassert Nigeria's commitment to peace, to development, to unity, to multilateralism and to the defence of human rights as beyond compromise. For none of us is safe until all of us are safe.

The road ahead will not be easy and we know there are no quick fixes to the trials that test the human spirit. Yet history reminds us that bold action in pursuit of noble ideals has always defined the story of the United Nations. Time and again, we have found the wisdom to balance sovereign rights with collective responsibility. That balance is once again in question.

But I believe, quite passionately, that a renewed commitment to multilateralism, not as a slogan but as an article of faith, remains our surest path forward. Nigeria dedicates itself fully and without reservation to that noble cause.
"""

ruto_speech = """
REPUBLIC OF KENYA

NATIONAL STATEMENT BY HIS EXCELLENCY HON. WILLIAM SAMOEI RUTO, Ph.D., C.G.H., PRESIDENT OF THE REPUBLIC OF KENYA AND COMMANDER-IN-CHIEF OF THE DEFENCE FORCES, AT THE GENERAL DEBATE OF THE 80TH SESSION OF THE UNITED NATIONS GENERAL ASSEMBLY

SEPTEMBER 24, 2025

NEW YORK, USA

The President of the 80th Session of the UN General Assembly, Ms Annalena Baerbock, Secretary-General of the United Nations, António Guterres, Excellencies, Heads of State and Government, Distinguished Delegates, Ladies and Gentlemen,

I congratulate you, Ms Annalena Baerbock, on your election to preside over the 80th Session of the UN General Assembly. Madam President, you can count on Kenya's full support throughout your tenure as you steer the Assembly into the future.

Ladies and gentlemen, 80 years ago, in the aftermath of unprecedented global destruction and devastating war, the international community came together in hope. They created this Organisation - the United Nations - as a shield against the horrors of war, as a platform for dialogue, and as a bridge to a better, fairer, more secure global community.

What is often forgotten, or not mentioned today, is that the United Nations grew out of the failure of the League of Nations, which existed between 1919 and 1945. The League of Nations did not collapse for lack of good intentions or noble objectives. Formed at the end of the First World War, and as part of the Treaty of Versailles, it was humanity's first attempt to build a permanent international organisation to stop aggression, end war, and bring nations together. Its ambitions were to achieve collective global security, disarmament, peaceful dispute resolution, and cooperation on humanitarian and social issues.

Despite these ideals, the League of Nations faltered. The United States never joined; other great powers came and went, and without enforcement authority, its condemnations carried little weight. When Japan invaded Manchuria, when Italy marched into Ethiopia, and when Hitler openly defied its rules, the League stood by, helpless and powerless. By the late 1930s, its credibility had collapsed, and with the outbreak of World War II, it was rendered irrelevant.

Madam President, this history is both a lesson and a warning. Institutions rarely fail because they lack vision or ideals; more often, they drift into irrelevance when they do not adapt, when they hesitate to act, and when they lose legitimacy. To remain relevant, institutions must be re-imagined, reformed, renewed, and aligned with emerging realities.

Eight decades ago, the founders of the UN sought to correct the failures of the League by creating a stronger, more inclusive organisation, anchored in the principle of 'We the peoples of the United Nations, determined to save succeeding generations from the scourge of war'. Today, as we gather for the UN@80, the question is unavoidable: Is the United Nations relevant to the demands of our time? Can it continue to serve humanity in the face of current realities? Or has it become a relic of a bygone era?

Madam President, Excellencies, we meet against a grim global backdrop. Conflict rages in Eastern Europe, the Middle East, the Sahel, the Horn of Africa, and beyond. Climate disasters grow fiercer by the year. Inequality deepens, pandemics loom, and technological disruption outpaces governance. Instead of trust, mistrust is spreading. Instead of solidarity, fragmentation is taking root. In place of hope, anxiety fills our global community. We are living, to borrow from the words of the founders of this institution, not in 'larger freedom,' but in growing uncertainty.

At this moment of turbulence, when we most need a strong United Nations, the organisation faces its deepest crisis in credibility and capacity. Funding cuts have paralysed its operations. Bureaucracy has slowed its response. The Security Council remains frozen in the post-war structures of 1945, unable to act inclusively, with fairness and with speed. Ladies and Gentlemen, I can, however, state with absolute conviction that the United Nations has been one of humanity's greatest achievements. For eight decades, it has held back the spectre of global war, calmed conflicts from Cambodia to Liberia, and stood guard in some of the world's most dangerous places through the courage of its peacekeepers. Few institutions in human history can claim such a legacy.

The UN has stood at the frontlines of humanitarian crises: From famine relief in the Horn of Africa to emergency shelter for millions of Syrian and Ukrainian refugees. It was at the forefront in the eradication of smallpox, coordinated global responses to HIV/Aids, Ebola, and COVID-19, and continues to champion universal vaccination. Its agencies have advanced women's rights, protected children, safeguarded refugees, and set global norms on everything from disarmament to climate action. The UN's Sustainable Development Goals remain a shared blueprint for human progress. These are achievements no nation could have accomplished alone, however rich or great.

And yet, every institution, no matter how noble its origins or impactful its legacy, must adapt to changing times or slide into irrelevance. Today, the United Nations stands at a crossroads of renewal or decay. Put differently, after 80 years, the rhymes of time are calling on us to re-imagine the original promise that inspired the founding of the United Nations: the quest for global peace, development, and human rights. But this call must now be answered in a global context that is profoundly different from the post-war era in which the UN was conceived.

We would be denying the cold, hard truth if we said that the United Nations is delivering as it should. On peace and security, its voice is too often drowned out by the rivalries of great powers, while some nations simply ignore its resolutions and do as they please. Too often, the UN's Blue Helmet, once a symbol of moral authority, no longer commands the same respect. From the conflicts in Gaza and Ukraine to the crises in Sudan, DR Congo, Somalia, and the Sahel, we see actors proceed undeterred by the UN's calls.

Excellencies, Ladies and Gentlemen, Kenya speaks from the experience of a nation deeply invested in multilateralism. For decades, we have placed our troops and police in harm's way for peacekeeping missions across Africa and beyond— from Somalia to the Democratic Republic of Congo; from South Sudan to, most recently, Haiti. Over the past 15 months, we are proud to have led the Multinational Security Support (MSS) mission in Haiti, not because it has been easy, but because solidarity is the essence of the United Nations.

Madam President, the mandate of the MSS mission is coming to an end in a few days. As the lead nation, allow me to briefly share our experiences— the successes and the challenges— as both a cautionary tale and a living lesson about the strengths and weaknesses of the current global governance architecture.

For far too long, the people of Haiti called out to the world. Too often, their pleas were met with silence, hesitation, or half-measures. Haiti became a tragic reminder of what happens when the international community looks away, prevaricates, or offers half-hearted support. When Kenya responded to the request of the Haitian authorities, it was in the belief that we were joining a genuinely multinational effort. We welcomed and fully embraced Resolution 2699, by which the United Nations Security Council authorised the MSS with Kenya as the lead nation.

Drawing on our decades of peace support operations, we stepped forward, offered to lead, and deployed our officers to confront the rampant menace of gang violence in Port-au-Prince and its environs. Madam President, Ladies and gentlemen, the mission has operated in a volatile environment under enormous constraints. It has been underfunded, under-equipped, and operated below 40% of its authorised personnel strength. Our police officers have valiantly shouldered responsibilities without the full logistical support that should accompany any mission sanctioned by the United Nations.

Despite these challenges, and against all odds, the MSS has delivered results many thought were impossible. The Presidential Palace, once under siege from gangs, is today restored as the seat of government. The police headquarters and the police training academy, once overrun by gangs, are now secure, with the academy resuming the training of new officers, over 700 of whom graduated a few months ago. Schools that had been shuttered by violence have reopened, with children back in class, learning and progressing. Roads once manned or blocked by gangs have free-flowing traffic. Cases of kidnapping and extortion have reduced sharply. The airport and seaport, once surrounded by gangs, are now abuzz with normal operations.

Which begs the question: If so much could be achieved with limited resources and stretched personnel, within just 15 months, what more could have been accomplished if the United Nations fraternity had truly acted together in solidarity with the people of Haiti? From this podium, I wish to assure all partners and actors that, with the right personnel, adequate resources, appropriate equipment, and necessary logistics, Haiti's security can be restored. Gangs can be neutralised, and the safety of streets, schools, hospitals, and homes secured. The continued harassment, abductions, and criminal acts undermining the lives of Haitians are unacceptable and unjustifiable, and must be stopped.

Madam President, as the UN Security Council deliberates on the next steps, we must not lose sight of the fact that the situation in Haiti demands sustained, coordinated, and undivided international attention. A careful and orderly transition from the MSS is essential to consolidating the hard-won gains so far achieved. I urge the Security Council and all partners to remain steadfast in ensuring that Haiti moves forward on a path of peace, stability, and renewal.

Ladies and Gentlemen, on human rights, our principle is clear and unwavering: the protection of civilians and respect for humanitarian law cannot be applied selectively. We cannot condemn suffering in one place and turn a blind eye in another. Kenya is gravely concerned by the humanitarian catastrophe in Gaza, and by the immense suffering of civilians caught in the devastation of disproportionate military operations. At the same time, we call for the unconditional release of Israeli hostages. In line with the African Union and United Nations resolutions, we also call for a permanent ceasefire, for strict adherence to international humanitarian law, and for the launch of a credible political process. Only through such a process can the vision of a two-state solution be realised — where Israel and Palestine live side by side, in peace and in security.

Kenya is equally deeply troubled by the worsening humanitarian situation in Sudan, where innocent citizens are caught in the crossfire of a needless war. We fully endorse the Quad— comprising Egypt, Saudi Arabia, the United Arab Emirates, and the United States—in affirming that there can be no military solution and that only political dialogue offers a viable path forward. We join the Quad in urging all parties, including SAF, RSF, and external actors, to respect Sudan's sovereignty, unity, and territorial integrity, and firmly reject any attempts to divide the country, reaffirming our unwavering support for a unified Sudan for the benefit of its people.

Excellencies, distinguished delegates, those who look to the future with a clear vision know that climate change is not only the single greatest threat of our age, but also one of the greatest transformation opportunities of our time. The Global Stocktake has made it plain that the world is off track. Current Nationally Determined Contributions are steering us towards temperature rises far beyond any safe threshold. This is the difference between survival and devastation for millions across the world.

Kenya and Africa are not passive victims of this crisis. We are taking bold steps, showing that climate action is not only possible but can also be the foundation for inclusive growth. We are building a climate-resilient society by embedding adaptation into every sector: from agriculture and energy to infrastructure and livelihoods, to sustainable mining and artificial intelligence. This ambition is visible on the ground. Today, 93% of Kenya's electricity comes from renewable sources — geothermal, wind, solar, and hydro. We are expanding investments in e-mobility, climate-smart agriculture, clean cooking solutions, and green manufacturing. We are also pioneering nature-compatible solutions such as sustainable waste management and circular economy interventions.

Africa, too, is uniting its voice. In 2023, in Nairobi, we hosted the inaugural Africa Climate Summit, where the continent adopted the Nairobi Declaration on Climate Action and Call to Action. Just two weeks ago, in Addis Ababa, Africa came together once again at the second Africa Climate Summit to reaffirm our commitments and strengthen our ambition for climate-positive growth. We declared Africa not just as a victim of the crisis, but as a source of solutions — with climate action driving economic growth, transformation, and job creation for our communities.

Ambition, ladies and gentlemen, cannot stand on willpower alone. Implementing our new NDCs will require $56 billion. That is why we call on the global community to unlock the $300 billion agreed at Baku, and to accelerate negotiations toward the new $1.3 trillion goal under the Baku-Belém Roadmap. Without affordable finance and without reform of the international financial architecture, the promise of climate action in Africa will remain constrained.

Madam President, in the aftermath of World War II, the Bretton Woods institutions were created to stabilise the global economy and rebuild war-torn Europe. At the time, their design reflected the power and interests of the victorious nations, who were also their primary shareholders and beneficiaries. The IMF was tasked with upholding the gold standard exchange rate system, while the World Bank was established to finance Europe's reconstruction. Both have since evolved into development finance institutions, but their structures, decision-making, and governance remain dominated by wealthy countries.

Today, the global context is vastly different. The gold standard collapsed five decades ago, and Europe has long since been rebuilt. Yet the governance of these institutions has not kept pace with the needs of a multipolar world, especially the needs of poor and developing countries. The mismatch between shareholders and stakeholders has become starkly visible. For instance, during the IMF's recent allocation of Special Drawing Rights (SDRs), 64% went to wealthy countries with little need for liquidity support, while the poorest countries received just 2.4%. This imbalance highlights how the very institutions meant to safeguard global financial stability often perpetuate inequity.

I have argued, and I say it again, that the current global financial architecture punishes poor countries while rewarding the rich. Its rules, priorities, and allocation mechanisms consistently favour those already prosperous, while trapping vulnerable economies in cycles of debt, high borrowing costs, and inadequate access to emergency support. It is imperative to transform these institutions into genuinely independent, apolitical global bodies so that their operations are aligned with their global mandate. Such a shift would democratise decision-making, restore credibility, and allow the IMF and the World Bank to serve all countries fairly, rather than reinforcing old hierarchies.

But Africa is not merely waiting for external prescriptions. We are taking bold and deliberate steps to strengthen our financial independence, safeguard our stability, and accelerate our development. Kenya, for instance, fully endorsed the establishment of the Alliance of African Multilateral Financial Institutions, launched with the African Union in February 2024. This Alliance brings together our homegrown banks: Afreximbank, the Africa Finance Corporation, the Trade and Development Bank, Shelter Afrique, Africa Re, African Trade and Investment Development Insurance and ZEP-RE; institutions that embody Africa's determination to mobilise resources, finance trade, and build resilience on our own terms.

At the same time, the Africa Union is championing three transformative institutions: the African Central Bank, which will issue a single currency and free our trade from dependence on foreign money; the African Monetary Fund, positioned to stabilise our economies and give us true financial sovereignty; and the African Investment Bank, designed to mobilise resources for the infrastructure, industrialisation, and integration that Africa needs to rise. And to complete this vision, the African Credit Rating Agency, one that understands our realities, values our uniqueness, and tells our story with fairness and truth, has already been established.

Excellencies, as we mark the 80th anniversary of the United Nations, Africa also marks 20 years since the Ezulwini Consensus and the Sirte Declaration, the two historic milestones that established the Common African Position on UN Security Council reform. For two decades, Africa has spoken in one voice, demanding justice, equity, and representation in the highest organ of global governance. This demand, however, continues to be ignored, deferred, or endlessly debated to the detriment of both Africa and the legitimacy of the United Nations itself. You cannot claim to be the United Nations while disregarding the voice of 54 nations. Africa is no longer willing to wait on the margins of global governance, while decisions about peace, security, and development are made without our understanding, perspectives and voice. Africa's exclusion is not only unacceptable, unfair, and grossly unjust; it also undermines the very credibility of the United Nations.

Africa dominates most of the Security Council's agenda, provides some of the largest contingents to UN peacekeeping, and bears the heaviest costs of instability. Yet we remain the only continent without a permanent seat at the table, where decisions about our destiny are made. Africa deserves two permanent seats with full rights, including the veto, and two additional non-permanent seats on the UN Security Council. The world must understand that reforming the Security Council is not a favour to Africa; it is a necessity for the UN's own survival. If the UN is to remain relevant in this Century, it must reflect today's realities, not the post-war power arrangements of 1945.

Madam President, despite the stated and evident weaknesses of the United Nations, it remains humanity's best chance at global solidarity. No other institution has the universal legitimacy or convening power of the UN. From coordinating humanitarian relief in times of war and disaster, to mobilising the global response to Covid-19, to driving consensus on climate change through the Paris Agreement, the UN has consistently shown that the world can achieve together what no nation can accomplish on its own, however mighty. As Dag Hammarskjöld, the UN's second Secretary-General, once observed: 'The United Nations was not created to take humanity to heaven, but to save it from hell.' That mission is as urgent today as it was 8 decades ago.

At a time when conflicts are multiplying, when climate change threatens every economy, and when inequality is widening, the need for a functioning, credible, and effective multilateral system has never been greater. It is through the UN that nations have pooled resources to vaccinate billions of children, to protect refugees through the work of UNHCR, and to keep the peace in more than 70 missions worldwide. Without the UN, these achievements, as modest though they may sometimes seem, would not have been possible.

That is why we must resist the temptation to give up on the UN or abandon it. We must make it fit for purpose, reform its structures, strengthen its mandate, and ensure its decisions reflect today's realities rather than the geopolitical map of a bygone era. As one of the hosts of the UN headquarters, and the only one in the Global South, Kenya stands ready to do its part to enable the organisation to go through this phase of renewal successfully, as envisaged by the Secretary General, under UN@80 reforms.

In conclusion, Madam President, Ladies and Gentlemen, the 80th session of the UN General Assembly offers a critical moment for reflection, assessment, and re-commitment. It is a time for nations to ask hard questions and, more importantly, to take bold action. Kenya believes in the United Nations, in its principles, and in its potential. But we also believe that the UN, like all institutions, must evolve, adapt, and respond decisively to the realities of our time.

Let us take the courage to reform, the wisdom to act with justice, and the humility to listen to the voices of those most affected. The future of our children, the stability of our nations, and the survival of our planet depend on it.

I thank you.
"""

# Create DataFrame
speeches_df = pd.DataFrame({
    'country': ['Nigeria (Shettima)', 'Kenya (Ruto)'],
    'text': [shettima_speech, ruto_speech]
})

print("Speeches loaded successfully!")
print(f"Number of speeches: {len(speeches_df)}")

# ============================
# 2. TEXT PREPROCESSING FUNCTIONS
# ============================

def clean_text(text):
    """Clean and preprocess text"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^\w\s.,!?;]', '', text)
    return text.strip().lower()

def tokenize_text(text):
    """Tokenize text into words with error handling"""
    try:
        tokens = word_tokenize(text)
        # Remove punctuation and short words
        tokens = [word for word in tokens if word.isalpha() and len(word) > 2]
        return tokens
    except:
        # Fallback simple tokenization if NLTK fails
        words = text.split()
        return [word for word in words if word.isalpha() and len(word) > 2]

def remove_stopwords(tokens):
    """Remove stopwords from tokens"""
    try:
        stop_words = set(stopwords.words('english'))
        return [word for word in tokens if word not in stop_words]
    except:
        return tokens  # Return original tokens if stopwords not available

# ============================
# 3. SENTIMENT ANALYSIS
# ============================

def analyze_sentiment(text):
    """Analyze sentiment using TextBlob"""
    blob = TextBlob(text)
    return {
        'polarity': blob.sentiment.polarity,
        'subjectivity': blob.sentiment.subjectivity,
        'sentiment': 'positive' if blob.sentiment.polarity > 0 else 'negative' if blob.sentiment.polarity < 0 else 'neutral'
    }

print("\nAnalyzing sentiment...")
sentiment_results = []
for idx, row in speeches_df.iterrows():
    sentiment = analyze_sentiment(row['text'])
    sentiment_results.append({
        'country': row['country'],
        'polarity': sentiment['polarity'],
        'subjectivity': sentiment['subjectivity'],
        'sentiment': sentiment['sentiment']
    })

sentiment_df = pd.DataFrame(sentiment_results)

print("\n=== SENTIMENT ANALYSIS RESULTS ===")
print(sentiment_df)

# ============================
# 4. EMOTION ANALYSIS
# ============================

# Expanded emotion words dictionary
emotion_words = {
    'positive': ['peace', 'hope', 'development', 'cooperation', 'unity', 'progress', 'security', 'prosperity', 
                'success', 'achievement', 'strength', 'confidence', 'optimism', 'opportunity', 'growth',
                'innovation', 'renewal', 'transformation', 'solidarity', 'partnership'],
    
    'negative': ['war', 'conflict', 'violence', 'crisis', 'threat', 'danger', 'suffering', 'poverty',
                'failure', 'collapse', 'destruction', 'devastation', 'tragedy', 'catastrophe', 'instability',
                'chaos', 'turmoil', 'despair', 'fear', 'anxiety'],
    
    'trust': ['trust', 'confidence', 'faith', 'belief', 'credibility', 'reliability', 'integrity',
             'honesty', 'transparency', 'accountability', 'commitment', 'pledge', 'assurance'],
    
    'fear': ['fear', 'anxiety', 'worry', 'threat', 'danger', 'risk', 'uncertainty', 'apprehension',
            'insecurity', 'vulnerability', 'panic', 'dread'],
    
    'joy': ['joy', 'happiness', 'hope', 'optimism', 'success', 'achievement', 'pride', 'satisfaction',
           'celebration', 'accomplishment', 'triumph', 'delight'],
    
    'sadness': ['sadness', 'suffering', 'pain', 'loss', 'tragedy', 'grief', 'despair', 'misery',
               'hopelessness', 'melancholy', 'sorrow', 'regret'],
    
    'anger': ['anger', 'frustration', 'rage', 'outrage', 'resentment', 'bitterness', 'hostility',
             'indignation', 'fury', 'wrath', 'irritation'],
    
    'surprise': ['surprise', 'unexpected', 'shock', 'amazing', 'astonishing', 'remarkable',
                'extraordinary', 'unforeseen', 'sudden', 'unanticipated']
}

def analyze_emotions(text):
    """Analyze emotional content of text"""
    try:
        tokens = remove_stopwords(tokenize_text(clean_text(text)))
        emotion_counts = {emotion: 0 for emotion in emotion_words.keys()}
        
        for word in tokens:
            for emotion, words in emotion_words.items():
                if word in words:
                    emotion_counts[emotion] += 1
                    
        return emotion_counts
    except Exception as e:
        print(f"Error in emotion analysis: {e}")
        return {emotion: 0 for emotion in emotion_words.keys()}

print("\nAnalyzing emotions...")
emotion_results = []
for idx, row in speeches_df.iterrows():
    emotions = analyze_emotions(row['text'])
    emotions['country'] = row['country']
    emotion_results.append(emotions)

emotion_df = pd.DataFrame(emotion_results)

print("\n=== EMOTION ANALYSIS RESULTS ===")
print(emotion_df)

# ============================
# 5. WORD FREQUENCY ANALYSIS
# ============================

def get_word_frequencies(text, top_n=20):
    """Get most frequent words"""
    tokens = remove_stopwords(tokenize_text(clean_text(text)))
    if not tokens:
        return []
    
    freq_dist = nltk.FreqDist(tokens)
    return freq_dist.most_common(top_n)

print("\nAnalyzing word frequencies...")
word_freqs = {}
for idx, row in speeches_df.iterrows():
    word_freqs[row['country']] = get_word_frequencies(row['text'])

print("\n=== TOP WORDS BY SPEECH ===")
for country, freqs in word_freqs.items():
    print(f"\n{country}:")
    for word, count in freqs[:10]:
        print(f"  {word}: {count}")

# ============================
# 6. VISUALIZATION
# ============================

# Set style for better plots
plt.style.use('default')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 12

print("\nGenerating visualizations...")

# 6.1 Sentiment Comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Polarity and Subjectivity
colors = ['#1f77b4', '#ff7f0e']  # Blue and orange
ax1.bar(sentiment_df['country'], sentiment_df['polarity'], color=colors, alpha=0.7)
ax1.set_title('Sentiment Polarity Comparison', fontsize=14, fontweight='bold')
ax1.set_ylabel('Polarity (-1 to 1)')
ax1.set_ylim(-1, 1)
ax1.grid(True, alpha=0.3)

ax2.bar(sentiment_df['country'], sentiment_df['subjectivity'], color=colors, alpha=0.7)
ax2.set_title('Subjectivity Comparison', fontsize=14, fontweight='bold')
ax2.set_ylabel('Subjectivity (0 to 1)')
ax2.set_ylim(0, 1)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sentiment_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# 6.2 Emotion Analysis Visualization
emotion_melted = emotion_df.melt(id_vars=['country'], 
                                var_name='emotion', 
                                value_name='count')

plt.figure(figsize=(14, 8))
sns.barplot(data=emotion_melted, x='emotion', y='count', hue='country', palette='viridis')
plt.title('Emotional Tone Comparison: Shettima vs Ruto', fontsize=16, fontweight='bold')
plt.xlabel('Emotion Categories', fontsize=12)
plt.ylabel('Word Count', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Speech')
plt.tight_layout()
plt.savefig('emotion_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# 6.3 Word Clouds
def plot_wordcloud(text, title, max_words=100):
    """Generate and plot word cloud"""
    try:
        cleaned_text = clean_text(text)
        wordcloud = WordCloud(
            width=800, 
            height=400, 
            background_color='white',
            max_words=max_words,
            colormap='viridis',
            relative_scaling=0.5
        ).generate(cleaned_text)
        
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title(f'Word Cloud: {title}', size=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(f'wordcloud_{title.replace(" ", "_").replace("(", "").replace(")", "")}.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
    except Exception as e:
        print(f"Error generating word cloud for {title}: {e}")

# Generate word clouds
for idx, row in speeches_df.iterrows():
    plot_wordcloud(row['text'], row['country'])

# 6.4 Sentiment Trajectory
def plot_sentiment_trajectory(text, title, color):
    """Plot sentiment trajectory across sentences"""
    try:
        sentences = sent_tokenize(text)
        sentiments = [TextBlob(sentence).sentiment.polarity for sentence in sentences if len(sentence) > 10]
        
        plt.figure(figsize=(14, 6))
        plt.plot(range(len(sentiments)), sentiments, color=color, linewidth=2.5, alpha=0.8)
        plt.axhline(y=0, color='black', linestyle='--', alpha=0.3)
        plt.title(f'Sentiment Trajectory: {title}', fontsize=16, fontweight='bold')
        plt.xlabel('Sentence Number')
        plt.ylabel('Sentiment Polarity')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'sentiment_trajectory_{title.replace(" ", "_").replace("(", "").replace(")", "")}.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
    except Exception as e:
        print(f"Error plotting sentiment trajectory for {title}: {e}")

# Plot sentiment trajectories
colors = ['#1f77b4', '#ff7f0e']  # Blue and orange
for idx, row in speeches_df.iterrows():
    plot_sentiment_trajectory(row['text'], row['country'], colors[idx])

# ============================
# 7. TEXT STATISTICS
# ============================

def calculate_text_statistics(text, country):
    """Calculate various text statistics"""
    try:
        sentences = sent_tokenize(text)
        words = tokenize_text(clean_text(text))
        words_no_stopwords = remove_stopwords(words)
        
        return {
            'country': country,
            'word_count': len(words),
            'sentence_count': len(sentences),
            'avg_sentence_length': len(words) / len(sentences) if sentences else 0,
            'unique_words': len(set(words)),
            'lexical_diversity': len(set(words)) / len(words) if words else 0,
            'avg_word_length': np.mean([len(word) for word in words]) if words else 0
        }
    except Exception as e:
        print(f"Error calculating statistics for {country}: {e}")
        return {
            'country': country,
            'word_count': 0,
            'sentence_count': 0,
            'avg_sentence_length': 0,
            'unique_words': 0,
            'lexical_diversity': 0,
            'avg_word_length': 0
        }

print("\nCalculating text statistics...")
stats_results = []
for idx, row in speeches_df.iterrows():
    stats = calculate_text_statistics(row['text'], row['country'])
    stats_results.append(stats)

stats_df = pd.DataFrame(stats_results)

print("\n=== TEXT STATISTICS ===")
print(stats_df)

# Visualization of text statistics
stats_melted = stats_df.melt(id_vars=['country'], 
                            var_name='metric', 
                            value_name='value')

# Exclude country from metrics to plot
stats_to_plot = stats_melted[stats_melted['metric'] != 'country']

plt.figure(figsize=(14, 8))
sns.barplot(data=stats_to_plot, x='metric', y='value', hue='country', palette='coolwarm')
plt.title('Text Statistics Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.legend(title='Speech')
plt.tight_layout()
plt.savefig('text_statistics.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================
# 8. SUMMARY REPORT
# ============================

print("\n" + "="*60)
print("SUMMARY ANALYSIS REPORT")
print("="*60)

for idx, row in speeches_df.iterrows():
    country = row['country']
    text = row['text']
    
    # Basic stats
    word_count = len(tokenize_text(clean_text(text)))
    sentence_count = len(sent_tokenize(text))
    sentiment = analyze_sentiment(text)
    
    print(f"\n{country}:")
    print(f"  • Word Count: {word_count:,}")
    print(f"  • Sentence Count: {sentence_count}")
    print(f"  • Sentiment: {sentiment['sentiment']} (Polarity: {sentiment['polarity']:.3f})")
    print(f"  • Subjectivity: {sentiment['subjectivity']:.3f}")
    
    # Top 5 words
    top_words = get_word_frequencies(text, 5)
    if top_words:
        print(f"  • Top Words: {', '.join([word for word, count in top_words])}")

# ============================
# 9. COMPARATIVE ANALYSIS
# ============================

print("\n" + "="*60)
print("COMPARATIVE ANALYSIS")
print("="*60)

# Sentiment comparison
nigeria_sentiment = sentiment_df[sentiment_df['country'] == 'Nigeria (Shettima)'].iloc[0]
kenya_sentiment = sentiment_df[sentiment_df['country'] == 'Kenya (Ruto)'].iloc[0]

print(f"\n1. SENTIMENT ANALYSIS:")
print(f"   • Nigeria speech is more {nigeria_sentiment['sentiment']} (polarity: {nigeria_sentiment['polarity']:.3f})")
print(f"   • Kenya speech is more {kenya_sentiment['sentiment']} (polarity: {kenya_sentiment['polarity']:.3f})")

# Emotion comparison
nigeria_emotions = emotion_df[emotion_df['country'] == 'Nigeria (Shettima)'].iloc[0]
kenya_emotions = emotion_df[emotion_df['country'] == 'Kenya (Ruto)'].iloc[0]

print(f"\n2. DOMINANT EMOTIONS:")
# Find top 3 emotions for each
nigeria_top_emotions = sorted([(emotion, count) for emotion, count in nigeria_emotions.items() if emotion != 'country'], 
                             key=lambda x: x[1], reverse=True)[:3]
kenya_top_emotions = sorted([(emotion, count) for emotion, count in kenya_emotions.items() if emotion != 'country'], 
                           key=lambda x: x[1], reverse=True)[:3]

print(f"   • Nigeria: {', '.join([f'{emotion}({count})' for emotion, count in nigeria_top_emotions])}")
print(f"   • Kenya: {', '.join([f'{emotion}({count})' for emotion, count in kenya_top_emotions])}")

print(f"\n3. TEXT CHARACTERISTICS:")
nigeria_stats = stats_df[stats_df['country'] == 'Nigeria (Shettima)'].iloc[0]
kenya_stats = stats_df[stats_df['country'] == 'Kenya (Ruto)'].iloc[0]

print(f"   • Nigeria speech length: {nigeria_stats['word_count']:,} words")
print(f"   • Kenya speech length: {kenya_stats['word_count']:,} words")
print(f"   • Nigeria lexical diversity: {nigeria_stats['lexical_diversity']:.3f}")
print(f"   • Kenya lexical diversity: {kenya_stats['lexical_diversity']:.3f}")

print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("All charts have been saved as PNG files in the current directory.")
print("="*60)