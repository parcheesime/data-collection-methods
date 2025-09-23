# 🕸️ Introduction to Ethical Web Scraping

This repository contains a short 3–4 lesson unit designed to introduce **young adults** to the concepts, ethics, and techniques of web scraping.  
The lessons build on one another: starting with **ethics**, moving into **robots.txt exploration**, then into **basic scraping**, and finishing with **advanced scraping vs. APIs**.

---

## 📚 Lesson Sequence

### Lesson 1: What is Web Scraping & Why Ethics Matter
**Objective:**  
Students understand what web scraping is, why people do it, and the ethical/legal boundaries.

**Content:**
- Define scraping vs. APIs vs. manual data collection.
- Discuss positive uses (e.g., research, open data, personal projects) vs. harmful uses (e.g., data theft, crashing servers, copyright violation).
- Walkthrough examples:  
  - ✅ *Good*: scraping prices for a personal budget project.  
  - ❌ *Bad*: scraping copyrighted books to repost.

---

### Lesson 2: Reading & Respecting Websites (robots.txt)
**Objective:**  
Students learn how to check if scraping is permitted on a site.

**Content:**
- Introduce `robots.txt` files and how to find them.  
- Explain `Disallow` and `Allow` rules.  
- Discuss why respecting these rules is important for ethics and legality.

**Activity:**  
- Students look up `robots.txt` on a few websites and determine what can/cannot be scraped.  
- Example: `https://www.wikipedia.org/robots.txt`

---

### Lesson 3: Basic Scraping Techniques
**Objective:**  
Students learn to scrape simple data responsibly.

**Content:**
- Intro to `requests` + `BeautifulSoup` (or `pandas.read_html`).  
- Identify tags in HTML (e.g., headlines, tables).  
- Add basic best practices:  
  - Use headers with a `User-Agent`.  
  - Pause between requests (`time.sleep`).  

**Activity:**  
- Scrape a simple Wikipedia table or news headlines.  

---

### Lesson 4: Advanced Web Scraping Techniques
**Objective:**  
Students explore challenges and solutions when scraping modern, complex websites.

**Content:**
- **JavaScript-Rendered Pages**: using Selenium/Playwright or finding hidden JSON.  
- **Pagination & Infinite Scroll**: mimicking API calls or automating scrolling.  
- **Authentication & Sessions**: cookies, tokens, and login forms (ethically, with permission).  
- **Anti-Scraping Measures**: rate limits, CAPTCHAs, and ethical boundaries.  
- **Structured Data Sources**: scraping JSON embedded in HTML, GraphQL, or hidden form fields.  
- **Concurrency & Scaling**: using `asyncio` or frameworks like Scrapy.  

**Activity:**  
- Demo: Scrape data from a site that requires pagination (e.g., stepping through multiple pages).  
- Extension: Inspect a site’s network tab to find a hidden API endpoint.

---

### Lesson 5: When to Scrape vs. Use an API
**Objective:**  
Students compare scraping to using an official API and reflect on which is more ethical and efficient.

**Content:**
- APIs are structured, permitted, and stable.  
- Downsides: may require API keys or have rate limits.  
- Compare scraping NASA’s site vs. using the official [NASA API](https://api.nasa.gov/).  
- Ethics: prefer APIs when available, scrape responsibly only if allowed.

**Activity:**  
- Students scrape headlines from a site.  
- Then use an API to get similar data.  
- Reflection: Which method is easier? Which is more ethical?

---