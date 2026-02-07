Use this command to activate python virtual environment:
source venv/bin/activate

Streamlit is used as the framework, run with following command:
streamlit run src/flashcardApp.py

Link to Hackathon Submission:
https://devpost.com/software/voice-to-study-notes?ref_content=user-portfolio&ref_feature=in_progress

//////////////REFLECTION FROM HACKATHON SUBMISSION: 

Activity Description:

With this project, I wanted to gain experience with AI integration in software development. Previously, I have written simple object-oriented programs without using APIs or full stack development frameworks, but I knew this is something I should learn to prepare me for the industry. Since I am new to using AI like Gemini in my programs, I wasn't quite sure of it's capabilities and had to adapt my project as I went to fit the features made available to me. I used some AI (Gemini and Copilot) to enhance my understanding (this helped as it has been a while since I have worked in Python) and I know that as AI becomes more prevalent, I must learn to work alongside it.

The primary features I tested were generate_content (with transcription of audio recording) and testing out ThinkingConfig settings.

Technical Decisions and Challenges Faced:

I had challenges coming up with what kind of app I wanted to make, at first, I wanted to play around with image generation, but the AI client used in this hackathon was limited to image analysis rather than generation. I switched to designing a practical study app that made use of the Gemini 3's audio analysis features. After troubleshooting a few different frameworks, I landed on uses Streamlit as it was rather simple and had thorough documentation. Being somewhat new to coding with AI tools and Python, syntax errors were common, but by using AI tools and documentation, I was quickly familiarized with conventions and resolved issues. Lastly, I was on a strict time schedule with this project, but to optimize my learning, I devoted my entire weekend and an hour each day of the work week.

Contributions:

I worked on this project all by myself. Despite it being very simple, I am proud of all the different tools it taught me to use. I had previously been too intimidated with complicated APIs and AI features to try integrating them into my programs, but reading documentation and using AI tools that were provided by the hackathon helped me try more ambitious features that I may have not otherwise. I also would ask friends to join me next time to help me work on more features and practice modularization/teamwork on an AI project (as a preparation for future work in the industry)

Quality Assessment:

Although I am not completely satisfied with my project, I think it's a great starting point and I am inspired to continue adding to it and integrating Gemini or other AI models to enhance my programs. I know my project contains a fair amount of boilerplate code and isn't all that unique as a result of the help I sought from preexisting documentation and AI agents, but now that I have a somewhat solid grasp on Python and AI integration, I can try something more ambitious next time.

What's Next:

I would like to add more stylish UI (more colors and interactive elements) For flashcards, I would like to try making a Quizlet or Duolingo alternative (game-ify study practice) I think text transcription of recorded lectures would be cool too. Lastly, I want to try using docker or learning how to host my application so anyone can access it from the cloud.

Interesting Stuff I learned:

I learned a lot more of the concept of tokens with AI, I previously understood that AI usage had to be limited due to hardware demands, but now I know how certain actions (like deeper learning) use more resources. Setting up virtual environments/python interpreters was new to me as well, previously, I had only made executables in c/c++. Also, I learned how to prevent certain data from being included in the repo (with gitignore) and why this is so important to do (accidently public published my API key)

Overall, my project is very tiny and straightforward due to my time constraints, but I learned a ton about AI usage!
