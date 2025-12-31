# Website Specification Document
## Higher Education Executive Coaching & Consulting Platform

**Document Version:** 1.0
**Date:** December 31, 2025
**Launch Deadline:** January 26, 2026

---

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Business Overview](#business-overview)
3. [Target Audience & User Segments](#target-audience--user-segments)
4. [Website Goals & Key Performance Indicators](#website-goals--key-performance-indicators)
5. [Technical Platform & Infrastructure](#technical-platform--infrastructure)
6. [Site Architecture & Navigation](#site-architecture--navigation)
7. [Page-by-Page Specifications](#page-by-page-specifications)
8. [Design & Brand Guidelines](#design--brand-guidelines)
9. [Features & Functionality](#features--functionality)
10. [Integrations & Third-Party Services](#integrations--third-party-services)
11. [Content Strategy](#content-strategy)
12. [SEO Strategy](#seo-strategy)
13. [Accessibility Requirements](#accessibility-requirements)
14. [Security & Legal Compliance](#security--legal-compliance)
15. [Launch Readiness](#launch-readiness)
16. [Post-Launch Maintenance](#post-launch-maintenance)

---

## Executive Summary

This specification outlines a comprehensive website for a higher education executive coaching and consulting business. The primary objective is to build a conversion-focused, content-rich platform that serves three distinct audience segments (early career professionals, middle managers, and senior leaders) while maintaining a cohesive brand experience.

**Primary Conversion Goal:** Email list signup (target: 85% of first-time visitors)
**Secondary Goals:** Book sales, coaching inquiries, speaking engagements, workshop bookings, cohort enrollment
**Technical Approach:** Unified Zoho ecosystem for seamless data flow and automation
**Brand Position:** Premium executive service meets trusted resource hub (6.5/10 on formality scale)

---

## Business Overview

### Mission
Provide executive coaching and consulting services to higher education professionals, helping them navigate complex workplace challenges sustainably without sacrificing wellbeing.

### Core Value Proposition
Counter the misconception that higher education careers require sacrifice of mental, financial, or physical health. Position higher education as a financially viable and deeply fulfilling career path that can be navigated successfully and sustainably.

### Services Offered
1. **Early Career Coaching** - Navigate important elements of the job and workplace successfully
2. **Middle Manager Coaching** - Improve managing up, down, and across; position for promotion
3. **Leadership Coaching** - Navigate complex challenges and transitions
4. **Team Development** - Build stronger leadership teams
5. **Culture Consulting** - Cultivate healthy work cultures for retention and productivity
6. **Strategic Planning** - Plan and implement innovative, effective systems
7. **Speaking Engagements** - Conference presentations and webinars
8. **Campus Workshops** - On-site professional development
9. **Group Coaching Cohorts** - Small group coaching programs
10. **Retreats** - Leadership retreats for teams

### Revenue Streams
- Individual coaching sessions
- Group coaching cohorts (with enrollment limits and payment)
- Book sales (direct and retail links)
- Workbooks and digital products
- Speaking fees
- Workshop/consulting fees
- Paid webinar recordings

---

## Target Audience & User Segments

### Segment 1: Early Career Professionals
**Profile:** New to higher education, 1-5 years experience
**Pain Points:** Navigating workplace dynamics, learning institutional culture, career trajectory uncertainty
**Messaging Focus:** Foundational skills, workplace navigation, career development
**Lead Magnet Examples:** "First 90 Days in Higher Ed Success Guide," "Navigating Office Politics Workbook"

### Segment 2: Middle Managers
**Profile:** 5-15 years experience, managing teams, aspiring to leadership
**Pain Points:** Managing up and down, positioning for promotion, balancing competing priorities
**Messaging Focus:** Leadership skills, strategic positioning, management effectiveness
**Lead Magnet Examples:** "Managing Up Strategy Guide," "Promotion Positioning Toolkit"

### Segment 3: Senior Leaders
**Profile:** Directors, VPs, Presidents, C-suite in higher education
**Pain Points:** Complex institutional challenges, team building, culture transformation, strategic innovation
**Messaging Focus:** Executive-level coaching, consulting, speaking, organizational development
**Lead Magnet Examples:** "Leadership Team Assessment," "Culture Transformation Framework"

### Common Thread Across Segments
Universal understanding that higher education has become more complex and challenging. Everyone needs help navigating these complex challenges.

### Traffic Sources
- LinkedIn profile and posts (primary)
- Conference presentations
- Webinars
- Published book(s)
- Professional organization referrals
- Organic search (secondary)

---

## Website Goals & Key Performance Indicators

### Primary Goal
**Email list conversion rate:** 85% of first-time visitors join email list

### Success Metrics
1. **Form submissions** - Lead magnet downloads, service inquiries, questionnaire completions
2. **Page views** - Blog posts, service pages, landing pages
3. **Email list signups** - Total subscribers and segment breakdown
4. **Book sales** - Direct purchases through website
5. **Discovery call bookings** - Qualified consultations scheduled
6. **Cohort enrollments** - Paid program registrations

### Analytics Platform
Zoho Analytics (native integration with all Zoho services)

### Conversion Funnels
1. **Awareness → Email → Nurture → Book Purchase**
2. **Awareness → Email → Nurture → Coaching Inquiry → Discovery Call → Client**
3. **Awareness → Email → Nurture → Cohort Enrollment**
4. **Awareness → Email → Nurture → Speaking/Workshop Inquiry**

---

## Technical Platform & Infrastructure

### Recommended Platform
**WordPress** with the following stack:

**Why WordPress:**
- Supports complex requirements (member areas, e-commerce, content management)
- Robust plugin ecosystem for Zoho integration
- Routine content updates are simple (blog posts, lead magnets)
- Technical changes require developer support (as preferred)
- WCAG 2.1 AA accessibility achievable
- Scalable for future growth

**Alternative Consideration:**
If absolute simplicity is prioritized over full automation, a Zoho Sites + manual workflow approach is possible but will sacrifice user experience quality and automation.

### Core Technology Stack

**Content Management:**
- WordPress CMS (latest version)
- Gutenberg block editor for page building
- Advanced Custom Fields (ACF) for custom content types

**E-Commerce & Enrollment:**
- WooCommerce for product sales (books, workbooks, cohorts)
- WooCommerce Bookings or Events Manager for cohort enrollment with capacity limits
- Automatic closure when spots fill up

**Membership & Access:**
- Not needed (content delivered via email instead of member portal)

**Forms:**
- WPForms or Gravity Forms with Zoho integration

**SEO:**
- Yoast SEO or Rank Math

**Performance:**
- WP Rocket or similar caching plugin
- Image optimization (Smush or ShortPixel)
- CDN integration

**Security:**
- Wordfence or Sucuri
- SSL certificate (HTTPS)
- Regular backups
- Two-factor authentication for admin

### Hosting
**Zoho Sites** or **Managed WordPress hosting** (SiteGround, WP Engine, or Kinsta recommended for performance and security)

### Domain
- Primary domain: [Client-owned domain]
- Additional domains: Invisible 301 redirects to primary domain

### Payment Processing
**Zoho Payments**
- Native integration with Zoho ecosystem
- 2.9% + $0.30 per transaction (domestic cards)
- 4.4% + $0.30 per transaction (international cards)
- PCI DSS Level 1 compliant
- 2-day payout (or instant payout option)
- Supports Visa, Mastercard, Amex, Discover, ACH
- 135+ currencies

### Browser & Device Compatibility
- **Desktop Browsers:** Chrome, Firefox, Safari, Edge (latest 2 versions)
- **Mobile Browsers:** Safari (iOS), Chrome (Android)
- **Responsive Design:** Mobile-first approach
- **Target:** 50% mobile traffic, 50% desktop traffic

---

## Site Architecture & Navigation

### Primary Navigation Structure

**Recommended Main Menu:**

```
Home | About | Services ▼ | Resources | Blog | Contact
```

**Services Dropdown Menu:**
- For Early Career Professionals
- For Middle Managers
- For Senior Leaders
- Speaking & Workshops
- Group Coaching Cohorts

**Rationale:** Groups services by audience first (aligns with segmentation strategy), then by format (speaking/cohorts). Minimizes clicks while keeping navigation clean.

### Alternative Navigation Option:

```
Home | About | Work With Me ▼ | Resources | Blog | Shop | Contact
```

**Work With Me Dropdown:**
- 1:1 Coaching (with sub-items or single page with sections)
- Group Coaching
- Speaking & Workshops
- Consulting

**Shop:** Separate menu item for books, workbooks, digital products

**Decision Point:** Recommend Services dropdown with audience segmentation for better user journey clarity.

### Footer Navigation

**Column 1: Services**
- Coaching for Early Career
- Coaching for Middle Managers
- Leadership Coaching
- Speaking & Workshops
- Group Cohorts

**Column 2: Resources**
- Blog
- Newsletter Signup
- Lead Magnets Library
- Recorded Webinars

**Column 3: About**
- About [Name]
- Book
- Testimonials
- Contact

**Column 4: Legal**
- Privacy Policy
- Terms of Service
- Refund Policy
- Cookie Policy

**Column 5: Social & Newsletter**
- LinkedIn icon/link
- Newsletter signup CTA

### Secondary Navigation Elements

**Sticky Header (Mobile & Desktop):**
- Logo (links to homepage)
- Main menu
- "Join Newsletter" CTA button (prominent, contrasting color)

**Utility Navigation:**
- None needed (no user accounts/login for public site)

---

## Page-by-Page Specifications

### Homepage

**Purpose:** Serve all audience segments with clear pathways; drive email signups

**Hero Section:**
- **Headline:** Clear statement of who you help
  Example: "Navigate Your Higher Education Career Successfully—Without Sacrificing Your Wellbeing"
- **Subheadline:** Universal message about complexity + your solution
  Example: "Expert coaching and consulting for higher education professionals at every career stage"
- **Primary CTA:** "Join My Newsletter" (email capture)
- **Secondary CTA:** "Explore Services"
- **Visual:** Minimal—brand colors, clean typography, possibly one professional photo (not prominent)

**Services Overview Section:**
- Three-column layout for audience segments
- **Column 1:** Early Career Professionals
  - Icon/graphic
  - 2-3 sentence description
  - CTA: "Learn More"
- **Column 2:** Middle Managers
  - Icon/graphic
  - 2-3 sentence description
  - CTA: "Learn More"
- **Column 3:** Senior Leaders
  - Icon/graphic
  - 2-3 sentence description
  - CTA: "Learn More"

**Credibility Section:**
- PhD, certifications, years in higher ed, notable titles
- "As Featured In" or "Worked With" - logos of institutions/professional organizations
- Brief mention of published book

**Testimonials Section:**
- 3-6 rotating or static testimonials
- Mix of audience segments
- Include name, title, institution (if permitted)

**Latest Blog Posts:**
- 3 most recent posts
- Thumbnail (if images available), title, excerpt, "Read More" link

**Newsletter Signup (Repeated):**
- Simple embedded form
- Value proposition: "Get weekly insights on [benefit]"

**Footer:** [Standard footer across all pages]

---

### About Page

**Purpose:** Establish credibility and authenticity; build trust

**Content Structure:**

**Professional Bio (1 long paragraph):**
- Current role/expertise
- PhD, certifications, credentials
- Years in higher education + notable positions held
- Published book mention
- Your coaching/consulting philosophy in brief

**Credibility Indicators:**
- Institutions worked with (logos)
- Professional organizations
- Speaking engagements/conferences
- Publications/media features

**Call-to-Action:**
- "Ready to work together? [Schedule a Discovery Call]"
- "Join my newsletter for weekly insights"

**Photo:**
- One professional headshot (not prominent, but present)

**Tone:** Professionally focused, credentialed expert who is authentic and direct

---

### Service Pages (Individual Pages for Each)

#### Service Page Template Structure:

**1. Coaching for Early Career Professionals**
**2. Coaching for Middle Managers**
**3. Coaching for Senior Leaders**

Each page includes:

**Hero:**
- Page title
- 1-2 sentence value proposition for this segment

**Who This Is For:**
- Bullet points describing ideal client

**What You'll Gain:**
- Specific outcomes/benefits
- Addresses segment-specific pain points

**How It Works:**
- Coaching format (1:1 sessions, frequency, duration)
- Process overview

**Pricing (if displayed):**
- TBD based on client preference for transparency
- Or "Custom pricing based on your needs"

**Testimonials:**
- 2-3 testimonials from this segment

**Next Steps:**
- CTA: "Schedule a Discovery Call" (links to questionnaire + booking)
- Or "Learn more about my approach" (links to About)

---

#### Speaking & Workshops Page

**Content:**

**Speaking Engagements:**
- Conference presentations
- Webinars
- Keynotes

**Campus Workshops:**
- Professional development for staff
- Leadership team training
- Custom topic development

**Topics:**
- List of common speaking/workshop topics
- "Custom topics available"

**Past Engagements:**
- Logos of institutions/conferences where you've spoken
- Testimonials from event organizers

**How to Book:**
- CTA: "Inquire About Speaking" (custom form with specific questions)

**Form Fields for Speaking Inquiry:**
- Name, email, institution
- Event type (conference, workshop, webinar)
- Desired dates
- Audience size
- Topic interests
- Budget range (optional)

---

#### Group Coaching Cohorts Page

**Content:**

**Overview:**
- What group coaching is
- Benefits of group format vs. 1:1

**Current/Upcoming Cohorts:**
- Each cohort displayed as a card/section:
  - Cohort title
  - Dates & times
  - Duration (e.g., "8 weeks")
  - Curriculum/topics covered
  - Testimonials from past participants
  - Price
  - Spots remaining (dynamic)
  - "Enroll Now" button (if spots available)
  - "SOLD OUT" banner if full (watermark style across card)

**How It Works:**
- Session format
- Community/peer learning benefits
- Access to recordings and resources (delivered via email)

**Who Should Join:**
- Ideal participant profile

**FAQ:**
- Common questions about cohorts

**CTA:**
- "Enroll in [Cohort Name]" or "Join the Waitlist"

---

### Resources Library Page

**Purpose:** Browsable collection of all lead magnets and free resources

**Layout:**

**Filter/Category Options (if implementing blog categories later):**
- All Resources
- Early Career
- Middle Management
- Leadership
- [Topic categories TBD]

**Resource Cards:**
Each lead magnet displayed as a card:
- **Thumbnail/Icon**
- **Resource Title**
- **Short description** (1-2 sentences)
- **CTA:** "Download Now" (triggers email capture form)

**Resources Include:**
- Lead magnet PDFs
- Workbooks
- Recorded webinars (free)
- Video content
- Any other free resources

**Email Capture for Each Resource:**
- Modal/popup form when "Download Now" clicked
- Fields: Name, Email
- Checkbox: "Also subscribe to weekly newsletter" (optional)
- Submit → Thank you page → Email delivery

---

### Blog Page

**Purpose:** Demonstrate expertise; SEO; nurture potential clients

**Layout:**

**Blog Archive (Main Blog Page):**
- List of all blog posts in reverse chronological order
- Each post preview includes:
  - Title
  - Publication date
  - Excerpt (first 150 characters or custom excerpt)
  - "Read More" link
  - Optional: Featured image thumbnail

**Sidebar or Below Posts:**
- Newsletter signup form
- Popular posts
- Categories (if implemented later)

**Individual Blog Post Template:**

**Post Header:**
- Post title
- Publication date
- Reading time estimate (optional)

**Post Content:**
- Article body (rich text formatting)
- Subheadings, bullet points, images as needed

**Social Sharing:**
- Share to LinkedIn button (prominent)
- Share to Twitter/X (optional)
- Email share option

**Author Bio Box (end of post):**
- Small headshot
- Brief bio (2-3 sentences)
- Links: "Work with me" → Services, "Subscribe" → Newsletter

**Related Posts:**
- 3 related blog posts (algorithm-based or manual)

**Comments:**
- NOT enabled (one-way communication as specified)

**Newsletter Signup CTA:**
- Repeated at bottom of post
- "Enjoyed this? Get weekly insights delivered to your inbox"

---

### Contact Page

**Purpose:** General inquiries; multiple contact paths

**Content:**

**Get in Touch:**
- Brief intro: "I'd love to hear from you"

**Contact Options:**

**1. General Inquiry Form:**
- Name
- Email
- Subject
- Message
- Submit button

**2. Service-Specific Inquiries:**
- "Interested in coaching? [Schedule a Discovery Call]"
- "Book me to speak at your event: [Speaking Inquiry Form]"
- "Questions about group cohorts? [Email link or form]"

**3. Direct Contact:**
- Email address (if public)
- LinkedIn profile link

**Office Hours/Response Time:**
- "I typically respond within 24-48 hours"

**Newsletter Signup:**
- "Not ready to reach out yet? Join my newsletter"

---

### Product/Shop Pages

**Shop Landing Page:**

**Product Categories:**
- Books
- Workbooks
- Digital Products
- Recorded Webinars (paid)

**Product Cards:**
Each product displayed with:
- Product image (book cover, workbook preview)
- Title
- Price
- Short description
- "Add to Cart" or "Buy Now"

**Individual Product Page Template:**

**Product Details:**
- Product images (multiple angles for physical products)
- Title
- Price
- Detailed description
- What's included
- Reviews/testimonials (if applicable)
- "Add to Cart"
- Quantity selector (if applicable)

**Related Products:**
- "You might also like..." (e.g., book + workbook bundle suggestion)

**Bundle Option:**
- Ability to purchase multiple products in one transaction
- "Buy Book + Workbook together and save"

**Cart & Checkout:**
- WooCommerce standard cart
- Zoho Payments integration for checkout
- Guest checkout enabled
- Account creation optional

**Order Confirmation:**
- Thank you page
- Order summary
- Delivery information (shipping for physical, download links for digital)
- "Join my newsletter" CTA

---

### Legal Pages

#### Privacy Policy
- Data collection practices
- Cookie usage
- Third-party integrations (Zoho, payment processors)
- User rights (GDPR compliance if applicable)
- Contact for privacy inquiries

#### Terms of Service
- Website usage terms
- Intellectual property
- Disclaimer of warranties
- Limitation of liability

#### Refund Policy
- Refund terms for digital products
- Refund terms for coaching/cohorts
- Process for requesting refunds
- Timeline for refunds

#### Cookie Policy
- What cookies are used
- Why (analytics, functionality)
- How to disable cookies
- Link to Privacy Policy

**Cookie Consent Banner:**
- Display on first visit
- "This site uses cookies for analytics and functionality. [Accept] [Learn More]"
- Learn More links to Cookie Policy

---

### Thank You Pages

**Lead Magnet Thank You Page:**

**Content:**
- "Thank you for downloading [Lead Magnet Name]!"
- "Check your email for your download link"
- "While you wait, here's what to expect:"
  - Brief teaser about upcoming book
  - Book title, subtitle, expected release/availability
  - "Pre-order now" or "Learn more" CTA
- Optional: Newsletter signup (if they didn't already subscribe)

**Newsletter Signup Thank You Page:**

**Content:**
- "Welcome! You're on the list."
- "Check your email to confirm your subscription"
- "Here's what you'll receive:"
  - Weekly newsletter description
  - What topics you'll learn about
- Book teaser section (as above)

**Purchase Thank You Page:**

**Content:**
- "Thank you for your purchase!"
- Order summary
- "What's next:"
  - Digital products: "Download your [product] now" + button
  - Physical products: "Your order will ship within [timeframe]"
- "Join my newsletter for more insights" (if not already subscribed)

**Discovery Call Booked Thank You Page:**

**Content:**
- "Your discovery call is scheduled!"
- Appointment details (date, time, timezone)
- "Check your email for calendar invitation"
- "Before our call:"
  - "Think about your biggest challenges"
  - "Review my services: [link]"
  - "Join my newsletter for insights: [form]"

---

## Design & Brand Guidelines

### Brand Personality
**Attributes:** Highly credentialed, respected expert who is rigorously authentic, accessible, supportive, actionable, unexpected (says things people think but don't say out loud), caring, wise, direct, funny

**Formality Level:** 6.5/10
- Balance of premium executive service + trusted colleague resource
- Professional but not stuffy
- Credible but approachable

### Visual Design Philosophy

**Recommended Approach:**
**Clean, content-forward design with strategic visual interest**

**Rationale for Higher Ed Audience:**
- Higher ed leaders value substance over flash
- Credibility comes from content, not imagery
- Efficiency and scannability respected
- Organized layouts demonstrate respect for their time

**Design Elements:**

**Typography:**
- Strong, readable fonts (client's brand fonts from brand kit)
- Generous line spacing for readability
- Clear hierarchy (H1, H2, H3, body, captions)
- Minimum 16px body text (accessibility)

**White Space:**
- Generous margins and padding
- Uncluttered layouts
- Content sections clearly defined

**Color Usage:**
- Client's brand color palette (from brand kit document)
- Strategic pops of color for CTAs and highlights
- Purposeful use, not overwhelming
- High contrast for accessibility (WCAG AA minimum)

**Visual Elements:**
- Custom graphics/icons preferred over stock photography
- Illustrations or abstract shapes for section breaks
- Minimal photography (1-2 professional photos of client, not prominent)
- No stock photos of generic "business people"

**Layout:**
- Scannable section-based layouts
- Clear visual hierarchy guides the eye
- Consistent spacing system
- Grid-based structure

**Avoid:**
- Slider carousels (poor UX, accessibility issues)
- Excessive animation
- Auto-playing video
- Busy backgrounds
- Too many competing CTAs on one page

### Brand Kit Integration
Client will provide document after hire containing:
- Logo files (various formats)
- Color palette (hex codes)
- Typography (font families, weights, sizes)
- Brand personality details
- Specific design elements to avoid

### Photography Guidelines
- Maximum 1-2 professional photos of client on entire site
- Photos should not be focal points
- No stock photography
- If needed: custom graphics, illustrations, or icons instead

### Humor & Personality
- Small pops of humor in copy (not design)
- Direct, sometimes unexpected statements in headlines/subheadings
- Maintain professional credibility while being relatable

---

## Features & Functionality

### Email Capture & Lead Generation

**Newsletter Signup Forms:**

**Placement:**
- Sticky header (persistent CTA button)
- Homepage (hero section + repeated section)
- Footer (all pages)
- Blog sidebar or end of posts
- Embedded in relevant pages

**Form Fields:**
- Name (first name + last name, or just first name)
- Email address
- Submit button

**Behavior:**
- No intrusive popups (non-intrusive as specified)
- No exit-intent popups
- No scroll-triggered popups
- Clean embedded forms only

**Form Integration:**
- Connected to Zoho Campaigns
- Tags contacts as "Newsletter Subscriber"

---

**Lead Magnet Forms:**

**Placement:**
- Dedicated landing page for each lead magnet
- Resources library (modal/popup when "Download" clicked)

**Form Fields:**
- Name
- Email
- Optional checkbox: "Also subscribe to my weekly newsletter"

**Behavior on Submit:**
1. Form submits to Zoho Campaigns
2. Contact tagged with specific lead magnet name (e.g., "Lead Magnet: Early Career Guide")
3. Contact segmented by audience type in Zoho CRM
4. Redirects to "Thank You" page
5. Automated email sent with download link to lead magnet (via Zoho Campaigns)

**Welcome Email Sequence:**
- Lead magnet download email includes offer to join newsletter (if not already subscribed)
- Newsletter signup confirmation includes mention of lead magnets available

**Cross-Promotion:**
- If someone signs up via lead magnet, welcome email offers newsletter
- If someone signs up for newsletter, welcome email mentions lead magnets

---

### Service Inquiry & Booking System

**Discovery Call Booking (for qualified leads):**

**Access:**
- NOT prominently available site-wide
- Only offered after interest shown:
  - Link on service pages ("Ready to discuss coaching?")
  - Link in email nurture sequences
  - Mentioned on contact page

**Process:**
1. User clicks "Schedule a Discovery Call"
2. Lands on **questionnaire page** (qualifying questions)
3. After questionnaire submission → redirects to **calendar booking** (Zoho Bookings)

**Questionnaire Form Fields:**
- Name
- Email
- Current role/title
- Institution
- Which service interests you? (dropdown: Early Career Coaching, Middle Manager Coaching, Leadership Coaching, Speaking/Workshop, Consulting, Group Cohort, Other)
- What are your biggest challenges right now? (text area)
- What are you hoping to achieve through coaching/consulting? (text area)
- How did you hear about me? (dropdown)
- Anything else I should know before our call? (optional text area)

**After Questionnaire Submission:**
- Automatically routes to Zoho Bookings calendar
- Pre-fills name and email into booking form
- User selects available time slot
- Confirmation email sent (via Zoho Bookings)

**Calendar Integration:**
- Zoho Bookings manages availability
- Syncs with your calendar
- Automated reminders sent before call
- Meeting link included (Zoom/Google Meet/phone as configured)

**Data Flow:**
- Questionnaire responses saved in Zoho CRM
- Contact tagged as "Discovery Call Requested"
- Assigned to appropriate service segment based on questionnaire answers

---

**Service-Specific Inquiry Forms:**

**Speaking/Workshop Inquiry Form:**

**Form Fields:**
- Contact name
- Email
- Institution/Organization
- Event type (dropdown: Conference, Workshop, Webinar, Keynote, Other)
- Preferred dates (or "Flexible")
- Expected audience size
- Audience type (dropdown: Early career, Mid-level, Senior leadership, Mixed)
- Topic interests (checkboxes or text area)
- Event location (on-campus, virtual, other)
- Budget range (optional dropdown)
- Additional details (text area)

**Form Behavior:**
- Submits to Zoho CRM
- Tagged as "Speaking Inquiry"
- Notification sent to you
- Auto-response to inquirer: "Thank you, I'll respond within 24-48 hours"

---

**Cohort Inquiry Form (if applicable):**

**Note:** Most cohort interactions will be direct enrollment via shop page, but this form is for general questions.

**Form Fields:**
- Name
- Email
- Which cohort are you interested in? (dropdown)
- Questions or concerns (text area)

---

### E-Commerce & Product Sales

**Shopping Cart:**
- WooCommerce powered
- Persistent cart (saved even if user leaves site)
- "Add to Cart" buttons on product pages
- Mini cart icon in header showing item count

**Product Features:**

**Inventory Management:**
- Track stock for physical products (books, workbooks)
- Digital products: unlimited
- Cohorts: Limited capacity (set manually per cohort)

**Bundling:**
- Create product bundles (e.g., "Book + Workbook Bundle - Save 15%")
- Discounted bundle pricing
- Single "Add to Cart" for bundle

**Pricing:**
- Display prices clearly on all product pages
- Sale prices (if running promotions)
- Bundled savings highlighted

**Checkout Process:**

1. **Cart Review:**
   - Line items with quantities
   - Apply coupon code (optional feature)
   - Subtotal, tax (if applicable), total
   - "Proceed to Checkout"

2. **Checkout Form:**
   - Email address
   - Billing information
   - Shipping information (for physical products only)
   - Order notes (optional)
   - Account creation optional (not required)

3. **Payment:**
   - Zoho Payments integration
   - Secure payment form
   - Accepted cards: Visa, Mastercard, Amex, Discover
   - ACH option for U.S. customers
   - PCI compliant

4. **Order Confirmation:**
   - Thank you page
   - Order summary
   - Email confirmation sent
   - Download links for digital products (immediate)
   - Shipping information for physical products

**Post-Purchase:**
- Order confirmation email (automated)
- Shipping notification (for physical products)
- Digital delivery (immediate download links)
- Option to join newsletter (if not already subscribed)

**Zoho Integration:**
- Purchase data flows into Zoho CRM
- Customer contact record created/updated
- Tagged as "Customer"
- Enables targeted email campaigns (e.g., "Purchased book → invite to cohort")

---

### Cohort Enrollment System

**Requirements:**
- Enrollment with payment
- Limited spots
- Automatic closure when capacity reached
- Sold-out cohorts remain visible with "SOLD OUT" banner

**Implementation:**

**WooCommerce + WooCommerce Bookings (or Events Manager):**
- Each cohort is a "bookable product" or "event"
- Set max capacity (e.g., 12 spots)
- Track enrollments in real-time
- When capacity reached: "Add to Cart" button automatically changes to "Sold Out"

**Cohort Product Page:**
- All details visible (dates, times, curriculum, testimonials)
- Enrollment counter: "4 spots remaining" (updates dynamically)
- Price displayed
- "Enroll Now" button (if spots available)

**Sold-Out Cohorts:**
- Remain on page
- Watermark-style "SOLD OUT" banner overlaid on cohort card/section
- Optional: "Join Waitlist" button (collects email for next cohort notification)

**Enrollment Process:**
1. User clicks "Enroll Now"
2. Cohort added to cart (treated as product)
3. Checkout process (as described in e-commerce section)
4. Payment via Zoho Payments
5. Order confirmation
6. Automated welcome email with cohort details (via Zoho Campaigns)

**Post-Enrollment Communication:**
- Automated email sequence via Zoho Campaigns:
  - Welcome email with cohort start date
  - Reminder emails before sessions
  - Session recordings + resources sent via email after each session
  - No need for member portal (all delivered via email)

**Zoho Integration:**
- Enrollment data in Zoho CRM
- Contact tagged with cohort name (e.g., "Cohort: Spring 2026 Leadership")
- Segmented for cohort-specific emails

---

### Content Delivery (Cohort Recordings & Resources)

**Method:** Email-based delivery (no member portal required)

**Process:**
1. After each cohort session, manually upload recording + resources to website (private, non-indexed pages or cloud storage)
2. Send email via Zoho Campaigns to cohort participants with:
   - Session summary
   - Link to recording
   - Link to downloadable resources (PDFs, workbooks, etc.)
   - These links can be publicly accessible or password-protected (simple password shared with cohort)

**Time-Limited Access:**
- Resources available until cohort end date
- After cohort ends, links can be deactivated or archived
- Manual process (client manages when to remove/archive)

**Alternative for Security:**
- Host recordings on Vimeo (password-protected)
- Host resources on Google Drive with link-based access (no login required)
- Share links via email

---

### Blog Functionality

**Publishing:**
- WordPress editor (Gutenberg blocks)
- Schedule posts for future publication (batch writing workflow)
- Automatic publishing at scheduled time
- Automatic posting to Zoho Campaigns (if integration configured)

**Blog-to-Email Workflow:**

**Option 1: Write in WordPress, auto-send via Zoho Campaigns**
- Use Zapier or native Zoho integration
- When new blog post published → automatically sends as email newsletter to subscribers
- Requires: Integration setup between WordPress and Zoho Campaigns

**Option 2: Write in Zoho Campaigns, manually post to WordPress**
- Batch-write newsletters in Zoho Campaigns
- Schedule email sends
- Manually copy content to WordPress and publish as blog post
- More control, but requires double entry

**Recommendation:** Option 1 (auto-send) if integration is reliable and allows for email-specific formatting. Option 2 if you want to customize newsletter emails differently from blog posts.

**Blog Features:**
- Categories (optional, not implemented at launch but available later)
- Tags (optional)
- Featured images (optional)
- Author bio box (end of each post)
- Social sharing buttons (LinkedIn prominent)
- Related posts suggestions
- Newsletter signup CTA (bottom of post)
- No comments (one-way communication)

**RSS Feed:**
- Automatically generated by WordPress
- Allows subscribers to follow blog via RSS readers

---

### Search Functionality
**Not required** - Navigation and browsable resources library sufficient for launch

**Future Consideration:**
If content library grows significantly (100+ blog posts), can add search bar later.

---

### Social Media Integration

**LinkedIn:**
- LinkedIn icon in footer (links to profile)
- Social share button on blog posts (prominently placed)
- Optional: Embed LinkedIn posts/feed on homepage or blog sidebar (requires plugin)

**LinkedIn Feed Widget (Optional):**
- Displays recent LinkedIn posts
- Placement: Homepage or sidebar
- Encourages visitors to follow on LinkedIn

**Other Social Media:**
- Currently: LinkedIn only
- Expandable in future if other platforms become relevant

---

### Analytics & Tracking

**Zoho Analytics:**
- Native integration with all Zoho products
- Tracks:
  - Email signup sources (which lead magnet, which page)
  - Form submissions
  - Product purchases
  - Page views and user behavior

**Additional Tracking (Optional):**
- Google Analytics 4 (for website traffic analysis)
- Facebook Pixel (if planning future ads)
- LinkedIn Insight Tag (if planning LinkedIn ads)

**Cookie Consent:**
- If using tracking pixels/analytics, cookie consent banner required
- "This site uses cookies for analytics. [Accept] [Manage Settings]"
- Links to Cookie Policy

**Privacy Compliance:**
- GDPR-compliant (even if not required, best practice)
- Privacy Policy clearly states what's tracked
- Users can opt out of analytics

---

### Mobile Optimization

**Mobile-First Design:**
- All layouts responsive
- Touch-friendly buttons and forms (minimum 44x44px tap targets)
- Readable text without zooming (minimum 16px)
- Fast loading on mobile networks

**Mobile-Specific Considerations:**

**Navigation:**
- Hamburger menu for main navigation on mobile
- Sticky header with logo + menu toggle
- Newsletter CTA button visible in header

**Forms:**
- Large, easy-to-tap input fields
- Minimal required fields to reduce friction
- Keyboard-friendly input types (email keyboard for email fields, etc.)

**Blog Posts:**
- Readable paragraphs (shorter on mobile)
- Ample line spacing
- Images scale to fit screen

**Checkout:**
- Simplified mobile checkout flow
- Autofill-friendly forms
- Large "Pay Now" button

**Testing:**
- Test on iOS (Safari) and Android (Chrome)
- Test on various screen sizes (phones, tablets)

---

## Integrations & Third-Party Services

### Zoho Ecosystem

**Zoho CRM:**
- Central hub for all contact data
- Segments:
  - Newsletter subscribers
  - Lead magnet downloaders (tagged by specific magnet)
  - Service inquiries (coaching, speaking, consulting)
  - Customers (purchased products or enrolled in cohorts)
  - Discovery call prospects

**Data Flow into CRM:**
- All form submissions create/update contact records
- Tags applied based on action (e.g., "Lead Magnet: Manager Guide")
- Custom fields: Service interest, audience segment, inquiry type

**Zoho Campaigns (Email Marketing):**
- Newsletter distribution
- Welcome sequences
- Lead magnet delivery
- Cohort communication
- Automated nurture campaigns

**Email Lists & Segmentation:**
- Master list: All subscribers
- Segments within Zoho Campaigns:
  - Early Career (based on lead magnet or self-identification)
  - Middle Managers
  - Senior Leaders
  - Customers (purchased products)
  - Cohort participants (by cohort name)

**Automated Emails:**
- Welcome email (newsletter signup)
- Lead magnet delivery email
- Discovery call confirmation
- Purchase confirmations
- Cohort welcome and session notifications

**Zoho Bookings (Calendar Scheduling):**
- Discovery call scheduling
- Integrates with your calendar (Google/Outlook)
- Customizable availability
- Automated reminders
- Meeting link generation (Zoom, Google Meet, etc.)

**Zoho Payments:**
- Payment processing for all e-commerce transactions
- Integrated with WooCommerce (via Zoho Commerce API or payment gateway plugin)
- Secure, PCI-compliant
- Transaction data flows into Zoho CRM

**Zoho Forms (Optional):**
- Can use Zoho Forms for all form submissions if preferred over WordPress forms
- Directly integrates with Zoho CRM
- Embeddable on WordPress pages

**Zoho Analytics:**
- Dashboard for all key metrics
- Custom reports:
  - Email signup sources
  - Conversion funnel (visitor → email → customer)
  - Product sales
  - Lead magnet performance

---

### WordPress Plugins (Core Functionality)

**SEO:**
- Yoast SEO or Rank Math
- Schema markup for rich snippets
- XML sitemap generation
- Social media meta tags

**E-Commerce:**
- WooCommerce (core plugin)
- WooCommerce Zoho integration (if available, or custom API integration)
- WooCommerce Bookings or Events Manager (for cohort enrollment)

**Forms:**
- WPForms or Gravity Forms
- Zoho integration (via Zapier or native connector)

**Performance:**
- WP Rocket (caching)
- Image optimization (Smush, ShortPixel, or EWWW)
- Lazy loading for images

**Security:**
- Wordfence or Sucuri Security
- SSL certificate enforcement
- Login security (limit login attempts, two-factor authentication)

**Backup:**
- UpdraftPlus or BackupBuddy
- Automated daily backups to cloud storage (Google Drive, Dropbox, etc.)

**Accessibility:**
- WP Accessibility plugin (optional, for additional checks)
- Manual WCAG 2.1 AA compliance testing

---

### Third-Party Integrations (If Not Using Zoho for Everything)

**Email Marketing (if not Zoho Campaigns):**
- ConvertKit, Mailchimp, or ActiveCampaign (not recommended given Zoho commitment)

**Payment Gateway (if not Zoho Payments):**
- Stripe or PayPal (fallback option)

**Automation:**
- Zapier (connects WordPress forms to Zoho CRM/Campaigns if native integration unavailable)

---

## Content Strategy

### Launch Content Requirements

**Pages (Copy Needed):**
1. Homepage - All sections written and finalized
2. About - Bio paragraph finalized
3. Service pages (5 pages) - All content finalized
   - Coaching for Early Career Professionals
   - Coaching for Middle Managers
   - Coaching for Senior Leaders
   - Speaking & Workshops
   - Group Coaching Cohorts
4. Resources Library - Intro text + lead magnet descriptions
5. Contact - Brief copy for contact page
6. Legal pages - Privacy Policy, Terms, Refund Policy (can use templates)

**Blog Posts:**
- 4 initial blog posts written and ready to publish

**Lead Magnets:**
- 3 lead magnets completed (PDFs, workbooks, or videos)
- Titles and descriptions written

**Email Content:**
- Welcome email templates (newsletter, lead magnet delivery)
- Cohort confirmation emails (if launching cohorts immediately)

---

### Ongoing Content Plan

**Weekly Newsletter/Blog:**
- Published every [day of week, e.g., Tuesday]
- Batch-written in advance
- Scheduled for automatic publishing

**Lead Magnet Expansion:**
- Add new lead magnets over time
- Each targets specific audience segment
- Promoted via newsletter and social media

**Recorded Webinars:**
- Upload past webinar recordings
- Offer free (with email capture) or paid

**Book Additions:**
- Second book added when ready
- Workbooks associated with books

**Cohort Updates:**
- New cohorts announced seasonally
- Previous cohort recordings potentially offered as standalone products

---

### Content Management Workflow

**Blog Publishing:**
1. Batch-write 4-8 blog posts
2. Upload to WordPress
3. Schedule for weekly publication
4. (Optional) Automate email distribution via Zoho Campaigns integration
5. Promote on LinkedIn after publishing

**Lead Magnet Creation:**
1. Create PDF/video/workbook
2. Upload to website (hosted file or cloud storage)
3. Create dedicated landing page
4. Write email delivery sequence in Zoho Campaigns
5. Add to Resources Library
6. Promote in newsletter

**Product Launches:**
1. Create product page in WooCommerce
2. Write sales copy
3. Upload product files (for digital products)
4. Set pricing
5. Announce in newsletter
6. Promote on LinkedIn

---

## SEO Strategy

### Target Keywords & Search Terms

**Research Recommended:** Full keyword research to identify high-value, low-competition terms

**Suggested Primary Keywords:**
- "higher education career coach"
- "higher education leadership consultant"
- "higher ed professional development"
- "college administrator coaching"
- "university leadership coaching"
- "higher ed career consulting"

**Long-Tail Keywords (Higher Intent):**
- "how to get promoted in higher education"
- "navigating higher ed workplace culture"
- "leadership coaching for university administrators"
- "higher education mid-career coaching"
- "sustainable career in higher education"

**Service-Specific Keywords:**
- "executive coaching for college presidents"
- "speaker for higher education conference"
- "campus leadership workshop facilitator"

**Blog Topic Keywords:**
- "managing up in higher education"
- "work-life balance higher ed"
- "higher education career transitions"
- "building leadership teams in universities"

---

### On-Page SEO

**Every Page Includes:**
- **Title Tag:** Keyword-optimized, under 60 characters
- **Meta Description:** Compelling summary, under 160 characters, includes CTA
- **H1 Tag:** One per page, includes primary keyword
- **Header Hierarchy:** Proper H2, H3 structure
- **Alt Text:** All images have descriptive alt text (accessibility + SEO)
- **URL Structure:** Clean, keyword-rich slugs (e.g., `/coaching-early-career-professionals/`)

**Homepage SEO:**
- Title: "[Your Name] - Higher Education Leadership Coach & Consultant"
- Meta Description: "Expert coaching for higher ed professionals at every career stage. Navigate your career successfully without sacrificing wellbeing. [CTA]"

**Service Page SEO:**
- Unique title and meta description for each
- Example: "Leadership Coaching for Higher Education Executives | [Your Name]"

**Blog Post SEO:**
- Title optimized for target keyword
- Internal linking to related posts and service pages
- External links to authoritative sources (when relevant)

---

### Technical SEO

**Site Speed:**
- Target: Under 3 seconds load time
- Optimized images (compressed, correct formats)
- Caching enabled
- Minified CSS/JavaScript
- CDN for static assets

**Mobile Optimization:**
- Responsive design (mobile-first)
- Google Mobile-Friendly Test passing
- Core Web Vitals optimized

**Schema Markup:**
- Organization schema (business information)
- Person schema (for About page)
- Article schema (blog posts)
- Product schema (shop items)
- Review schema (testimonials, if applicable)

**XML Sitemap:**
- Auto-generated by Yoast/Rank Math
- Submitted to Google Search Console

**Robots.txt:**
- Properly configured to allow search engines
- Block admin pages, thank-you pages (no index)

**SSL Certificate:**
- HTTPS enforced across entire site

---

### Off-Page SEO

**Backlink Strategy (Long-Term):**
- Guest posts on higher ed publications/blogs
- Speaking engagements (conference websites link to speaker bio)
- LinkedIn articles linking back to website
- Professional organization directories

**Local SEO (If Applicable):**
- Google Business Profile (if offering local services)
- Local citations (if relevant)

**Social Signals:**
- Active LinkedIn presence driving traffic
- Social sharing of blog posts

---

### Lead Magnet Landing Page SEO

**Strategy:**
- Each lead magnet has its own SEO-optimized landing page
- Can rank independently for specific search terms
- Example: "Free Guide: Navigating Your First Year in Higher Education"
  - URL: `/free-guide-first-year-higher-education/`
  - Optimized for "first year higher education" and related terms

**Benefits:**
- Multiple entry points from search engines
- Captures visitors at different stages of awareness
- Builds topical authority

---

## Accessibility Requirements

### Compliance Standard
**WCAG 2.1 Level AA** - Required for higher education institutional clients and brand values

### Accessibility Checklist

**Keyboard Navigation:**
- All interactive elements accessible via keyboard (Tab, Enter, Escape)
- Logical tab order
- Visible focus indicators (outline on focused elements)
- No keyboard traps

**Screen Reader Compatibility:**
- Semantic HTML (proper use of headings, lists, landmarks)
- ARIA labels where needed
- Alt text for all images (descriptive, not decorative)
- Form labels properly associated with inputs
- Skip-to-content link (hidden but available for screen readers)

**Color & Contrast:**
- Minimum contrast ratio: 4.5:1 for body text
- 3:1 for large text (18pt+ or 14pt+ bold)
- Color not used as only means of conveying information
- Links distinguishable from regular text (underline or other visual indicator)

**Text & Readability:**
- Minimum font size: 16px for body text
- Resizable text up to 200% without breaking layout
- Line height minimum 1.5 for body text
- Paragraph spacing 1.5x line height
- No text in images (unless decorative and alt text provided)

**Forms:**
- Clear labels for all fields
- Error messages clearly associated with fields
- Required fields indicated (not just by color)
- Helpful placeholder text (but not replacing labels)

**Multimedia:**
- Captions for videos (if using video content)
- Transcripts for audio (if using podcasts/webinars)
- No auto-playing media

**Interactive Elements:**
- Buttons clearly labeled (not just icons)
- Links have descriptive text (not "click here")
- Dropdown menus keyboard accessible
- Modals/popups can be closed with Escape key

**Testing:**
- Automated testing: WAVE, Axe, Lighthouse
- Manual testing: Keyboard-only navigation
- Screen reader testing: NVDA (Windows), JAWS, VoiceOver (Mac/iOS)

---

### Accessibility Statement (Optional Page)

**Content:**
- "We are committed to ensuring our website is accessible to all users"
- Compliance standard: WCAG 2.1 AA
- Contact information for accessibility concerns
- Known limitations (if any) and workarounds
- Timeline for addressing reported issues

---

## Security & Legal Compliance

### Website Security

**SSL Certificate:**
- HTTPS enforced across entire site
- Automatic redirect from HTTP to HTTPS

**WordPress Security:**
- Strong admin passwords
- Two-factor authentication for admin accounts
- Limit login attempts (prevent brute force attacks)
- Regular updates: WordPress core, themes, plugins
- File permissions properly configured
- Database security (unique prefixes, restricted access)

**Backup Strategy:**
- Automated daily backups
- Backups stored off-site (cloud storage)
- Tested restoration process
- Backup retention: 30 days minimum

**Malware & Threat Protection:**
- Wordfence or Sucuri (active monitoring)
- Firewall enabled
- Regular malware scans

**Form Security:**
- reCAPTCHA on forms (prevent spam)
- Email validation
- Input sanitization (prevent SQL injection, XSS)

**Payment Security:**
- PCI DSS compliance (handled by Zoho Payments)
- No credit card data stored on website
- Secure checkout (SSL + tokenization)

---

### Legal Pages (Required)

**Privacy Policy:**

Must include:
- What data is collected (name, email, payment info, browsing behavior)
- How data is used (newsletters, service delivery, analytics)
- Third parties with access (Zoho, payment processors, analytics)
- Cookie usage and tracking
- User rights (access, deletion, opt-out)
- Data retention policies
- Contact for privacy inquiries
- GDPR compliance (if applicable)
- CCPA compliance (if applicable - California residents)

**Terms of Service:**

Must include:
- Acceptable use of website
- Intellectual property rights (content ownership)
- Disclaimer of warranties
- Limitation of liability
- User responsibilities
- Termination of access (if applicable)
- Governing law and jurisdiction

**Refund Policy:**

Must specify:
- Digital products: Refund policy (e.g., "No refunds on digital downloads after access granted")
- Physical products: Return/refund terms and timeline
- Coaching/cohorts: Cancellation and refund policy
- Process for requesting refunds
- Timeline for processing refunds
- Contact for refund requests

**Cookie Policy:**

Must include:
- What cookies are used (essential, analytics, marketing)
- Why cookies are used (functionality, user experience, analytics)
- How to disable cookies
- Third-party cookies (Google Analytics, etc.)

---

### Cookie Consent Banner

**Required if using analytics/tracking cookies**

**Implementation:**
- Banner appears on first visit
- "This website uses cookies to improve your experience and analyze traffic. [Accept All] [Manage Preferences] [Learn More]"
- Learn More links to Cookie Policy
- User choice stored (cookie to remember preference, ironically)
- Compliant with GDPR/CCPA

---

### GDPR Compliance (Best Practice Even if Not Required)

**User Rights:**
- Right to access data
- Right to deletion ("Right to be Forgotten")
- Right to data portability
- Right to opt-out of marketing

**Implementation:**
- Contact form for data requests
- Process for handling requests within 30 days
- Unsubscribe link in all marketing emails (required by law)

---

### Email Compliance

**CAN-SPAM Act (U.S. Law):**
- Unsubscribe link in every email
- Accurate "From" and subject lines
- Physical mailing address in footer
- Process unsubscribe requests within 10 days

**GDPR (if applicable):**
- Explicit consent for email marketing (double opt-in recommended)
- Clear explanation of what emails subscriber will receive
- Easy unsubscribe process

---

### Intellectual Property

**Copyright:**
- Copyright notice in footer: "© [Year] [Your Name/Business Name]. All Rights Reserved."
- Protect original content (blog posts, lead magnets, course materials)

**Trademarks:**
- If business name or logo is trademarked, display ™ or ®

**User-Generated Content:**
- Not applicable (no comments or user uploads)

---

## Launch Readiness

### Content Deliverables (Client Responsibility)

**Text Content (Due Before Design Starts):**
- [ ] Homepage copy (all sections)
- [ ] About page bio
- [ ] Service pages (5 pages, all sections)
- [ ] Contact page copy
- [ ] Resources library intro
- [ ] 4 initial blog posts
- [ ] 3 lead magnet descriptions

**Visual Assets (Due Before Design Starts):**
- [ ] Brand kit document (logo, colors, fonts, guidelines)
- [ ] 1-2 professional photos (headshot, speaking photo)
- [ ] Lead magnet files (3 PDFs/workbooks/videos completed)

**Product Information:**
- [ ] Book details (title, description, pricing, cover image, ISBN if applicable)
- [ ] Workbook details (if launching at same time)
- [ ] Cohort details (if launching cohorts immediately: dates, times, curriculum, pricing)

**Email Templates:**
- [ ] Welcome email (newsletter)
- [ ] Lead magnet delivery email (can be templated)

**Domain & Accounts:**
- [ ] Domain name access (for DNS configuration)
- [ ] Zoho account setup (CRM, Campaigns, Bookings, Payments)

---

### Designer Deliverables

**Design Phase:**
- [ ] Sitemap and wireframes
- [ ] Homepage mockup (desktop + mobile)
- [ ] Interior page mockups (2-3 key pages)
- [ ] Style guide (typography, colors, button styles, spacing)

**Development Phase:**
- [ ] WordPress installation and configuration
- [ ] Theme development/customization
- [ ] All pages built and content integrated
- [ ] Zoho integrations configured
- [ ] WooCommerce setup (products, payment gateway)
- [ ] Forms created and tested
- [ ] Email templates in Zoho Campaigns
- [ ] Blog setup and initial posts published

**Testing Phase:**
- [ ] Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [ ] Mobile responsiveness testing (iOS, Android)
- [ ] Form submission testing (all forms)
- [ ] E-commerce testing (test purchases, refunds)
- [ ] Email automation testing (welcome sequences, lead magnet delivery)
- [ ] Accessibility testing (WCAG 2.1 AA compliance)
- [ ] SEO checklist (meta tags, sitemap, schema markup)
- [ ] Page speed optimization
- [ ] Security hardening

**Pre-Launch:**
- [ ] SSL certificate installed
- [ ] Google Analytics / Zoho Analytics configured
- [ ] Google Search Console setup
- [ ] Backup system configured and tested
- [ ] 301 redirects (if applicable from old site)
- [ ] Legal pages published
- [ ] Cookie consent banner configured
- [ ] Final client walkthrough and training

---

### Timeline (Due: January 26, 2026)

**Recommended Phases:**

**Week 1-2: Discovery & Planning**
- Client provides all content and assets
- Designer creates sitemap, wireframes
- Design mockups created
- Client feedback and revisions

**Week 3-4: Design Finalization & Development Start**
- Design approved
- WordPress setup begins
- Homepage and key pages built
- Zoho integrations configured

**Week 5-6: Full Development**
- All pages built
- WooCommerce and products configured
- Blog setup
- Forms and automations built

**Week 7: Testing & Refinement**
- Cross-browser/device testing
- Accessibility audit
- SEO optimization
- Client review and feedback
- Revisions

**Week 8: Pre-Launch & Launch**
- Final testing
- Content population (blog posts, lead magnets)
- Training for client on content management
- Go live on January 26, 2026

**Note:** This is an aggressive timeline. Success depends on:
- Client content ready on time
- Prompt feedback on design mockups
- Minimal revisions
- Designer availability and focus

---

## Post-Launch Maintenance

### Maintenance Plan Included (Recommended)

**Services Included:**
- **Software updates:** WordPress core, theme, plugins (monthly)
- **Security monitoring:** Malware scans, firewall updates
- **Backups:** Daily automated backups, tested quarterly
- **Uptime monitoring:** Alert if site goes down
- **Troubleshooting:** Same-day response for critical issues
- **Minor updates:** Small content changes, form updates (up to X hours/month)

**Excluded (Billed Separately):**
- Major redesigns
- New feature development
- Extensive content creation
- Marketing services

---

### Client-Managed Tasks (Post-Launch)

**Regular (Weekly):**
- Publish blog posts (draft in WordPress, schedule)
- Promote content on LinkedIn
- Check form submissions in Zoho CRM
- Respond to inquiries

**Monthly:**
- Review analytics (Zoho Analytics dashboard)
- Add new lead magnets (if applicable)
- Update cohort information (new dates, sold-out status)

**Quarterly:**
- Review and update service page copy (if needed)
- Add new products (books, workbooks)
- Review SEO performance and adjust strategy

**As Needed:**
- Update About page
- Add testimonials
- Adjust pricing
- Create new landing pages for campaigns

---

### Support & Training

**Designer Provides:**
- **Training session (1-2 hours):** How to publish blog posts, update pages, add products, manage forms
- **Video tutorials:** Screen recordings for common tasks
- **Documentation:** Written guide for content management

**Ongoing Support:**
- Email/ticket support for questions
- Same-day response for urgent issues (site down, critical bugs)
- 24-48 hour response for non-urgent questions

---

## Appendices

### A. Recommended Tools & Platforms

**Website Platform:** WordPress (self-hosted)
**Hosting:** Zoho Sites, SiteGround, WP Engine, or Kinsta
**Theme:** Custom theme or premium theme (Astra, GeneratePress, Kadence)
**Page Builder:** Gutenberg (native) or Elementor/Beaver Builder (optional)
**E-Commerce:** WooCommerce
**SEO:** Yoast SEO or Rank Math
**Forms:** WPForms or Gravity Forms
**CRM:** Zoho CRM
**Email Marketing:** Zoho Campaigns
**Calendar Booking:** Zoho Bookings
**Payment Processing:** Zoho Payments
**Analytics:** Zoho Analytics + Google Analytics 4
**Automation:** Zapier (if needed for integrations)

---

### B. Budget Considerations

**One-Time Costs:**
- Website design and development (designer quote)
- Premium theme (if applicable): $50-100
- Premium plugins: $100-500
- Stock images/graphics (if needed): $50-200
- SSL certificate: Often free (Let's Encrypt) or $10-100/year

**Ongoing Monthly/Annual Costs:**
- Hosting: $10-50/month (managed WordPress hosting)
- Zoho CRM: $14-52/user/month (depending on plan)
- Zoho Campaigns: $3-65/month (depending on subscriber count)
- Zoho Bookings: $6-12/user/month
- Zoho Payments: 2.9% + $0.30 per transaction (no monthly fee)
- Domain renewal: $10-20/year
- Plugin licenses: $50-200/year
- Maintenance plan: $100-500/month (if outsourcing)

**Estimated Total Ongoing:** $150-600/month depending on subscriber count and service usage

---

### C. SEO Keyword Research (To Be Completed)

**Deliverable:** Comprehensive keyword research document

**Includes:**
- 20-30 primary keywords with search volume and competition data
- Long-tail keyword opportunities
- Competitor analysis (top-ranking sites for target keywords)
- Content gap analysis (topics competitors rank for that you could target)
- Keyword mapping (which keywords to target on which pages)

**Tools for Research:**
- Google Keyword Planner
- Ahrefs, SEMrush, or Moz
- Google Search Console (post-launch)
- Answer the Public (question-based keywords)

---

### D. Content Calendar Template (First 3 Months)

**Weekly Blog Posts (Examples):**

**Month 1:**
- Week 1: "5 Things I Wish I Knew in My First Higher Ed Job"
- Week 2: "How to Navigate Institutional Politics Without Losing Yourself"
- Week 3: "Managing Up: What Your Boss Actually Needs from You"
- Week 4: "The Promotion Myth: Why Waiting Your Turn Doesn't Work Anymore"

**Month 2:**
- Week 1: "Building Leadership Teams That Actually Work Together"
- Week 2: "Why Burnout Culture Is a System Problem, Not a You Problem"
- Week 3: "The Art of Saying No (Without Torpedoing Your Career)"
- Week 4: "Leading Through Change When You're Exhausted by Change"

**Month 3:**
- Week 1: "What Makes a Good Mentor (and How to Find One)"
- Week 2: "Strategic Planning That Doesn't Gather Dust on a Shelf"
- Week 3: "Culture Change Starts With You—But It Can't End There"
- Week 4: "Sustainable Leadership: Working Smarter in Higher Ed"

**Lead Magnet Promotion Schedule:**
- Month 1: Promote "Early Career Success Guide"
- Month 2: Promote "Middle Manager Toolkit"
- Month 3: Promote "Leadership Team Assessment"

---

### E. Email Sequence Templates

**Newsletter Welcome Email (Example):**

**Subject:** Welcome! Here's what to expect.

**Body:**
Hi [First Name],

Thanks for joining my newsletter! I'm so glad you're here.

Every [day of week], you'll get insights on navigating your higher education career successfully—without sacrificing your wellbeing. I share strategies for managing up, positioning yourself for growth, building resilient teams, and leading through complexity.

Here's what you can expect:
- Practical advice you can actually use
- No fluff, just substance
- Perspectives you might not hear elsewhere (I say the quiet parts out loud)

While you're here, check out these free resources: [Link to Resources Library]

And if you haven't already, grab my book: [Link to Book]

Looking forward to being in your inbox,
[Your Name]

---

**Lead Magnet Delivery Email (Example):**

**Subject:** Your [Lead Magnet Name] is here!

**Body:**
Hi [First Name],

Thanks for downloading [Lead Magnet Name]! Here's your link:

[Download Button/Link]

I hope this [guide/workbook/toolkit] helps you [specific outcome].

**While you're here:** I send a weekly newsletter with more strategies like this. If you're not already subscribed, [join here].

**And one more thing:** I'm working on a book about [topic]—it's coming out [date]. [Learn more or pre-order here].

Thanks for being here,
[Your Name]

---

### F. Testing Checklist (Pre-Launch)

**Functionality Testing:**
- [ ] All navigation links work
- [ ] All forms submit correctly
- [ ] Form confirmation emails send
- [ ] Lead magnet delivery emails send with correct attachments
- [ ] Newsletter signup adds contacts to Zoho Campaigns
- [ ] Shopping cart adds/removes products correctly
- [ ] Checkout process completes successfully
- [ ] Payment processing works (test mode)
- [ ] Order confirmation emails send
- [ ] Discovery call booking works (integrates with calendar)
- [ ] Cohort enrollment works (capacity limits enforced)
- [ ] Blog posts display correctly
- [ ] Social share buttons work
- [ ] Search (if implemented) returns relevant results

**Cross-Browser Testing:**
- [ ] Chrome (Windows, Mac)
- [ ] Firefox (Windows, Mac)
- [ ] Safari (Mac, iOS)
- [ ] Edge (Windows)

**Responsive Testing:**
- [ ] iPhone (various sizes)
- [ ] Android phones (various sizes)
- [ ] iPad / tablets
- [ ] Desktop (1920px+, 1440px, 1024px)

**Accessibility Testing:**
- [ ] WAVE tool (no critical errors)
- [ ] Axe DevTools (no violations)
- [ ] Keyboard navigation (all interactive elements accessible)
- [ ] Screen reader test (NVDA or VoiceOver)
- [ ] Color contrast (all text passes WCAG AA)

**SEO Testing:**
- [ ] All pages have unique title tags
- [ ] All pages have meta descriptions
- [ ] XML sitemap generated and submitted
- [ ] Robots.txt configured correctly
- [ ] Schema markup implemented
- [ ] Google Search Console connected
- [ ] Page speed (Lighthouse score 80+)

**Security Testing:**
- [ ] SSL certificate installed (HTTPS)
- [ ] Security headers configured
- [ ] Login protection enabled
- [ ] Firewall active
- [ ] Backup system tested (restore from backup)

---

## Conclusion

This specification outlines a comprehensive, conversion-focused website for a higher education executive coaching and consulting business. The platform is designed to:

1. **Convert visitors to email subscribers** (85% target) through strategic lead magnets and clear CTAs
2. **Serve three distinct audience segments** with tailored messaging and pathways
3. **Automate key workflows** via unified Zoho ecosystem integration
4. **Establish credibility and trust** through professional design, testimonials, and content expertise
5. **Generate revenue** through book sales, cohort enrollments, and service inquiries
6. **Scale sustainably** with content management tools that empower the client

**Success depends on:**
- Timely delivery of all content and assets by client
- Expert design and development execution
- Robust Zoho integrations for seamless automation
- Accessibility and SEO best practices from day one
- Post-launch content consistency (weekly blog, email nurture)

**Launch Date:** January 26, 2026

This document should serve as the complete blueprint for the designer to build a world-class website that positions the client as the go-to expert for higher education professionals seeking sustainable, successful careers.

---

**Document Prepared By:** Claude Code
**Date:** December 31, 2025
**Version:** 1.0
**Next Steps:** Share with designer for quote and project kickoff
