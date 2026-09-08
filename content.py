# -*- coding: utf-8 -*-
"""
THE STRATEGIST - site content.

Sourced from the client's "The Strategist Website v2" document plus the
original BRD. Anything the client supplied verbatim is marked CLIENT.
Anything drafted by us for review is marked DRAFT and rendered on the
site with a "Draft copy" tag so the client can see what needs approval.
"""

SITE = {
    "name": "The Strategist",
    "tagline": "From Vision to Victory",
    "positioning": "Strategy. Performance. Transformation.",
    # CLIENT (BRD s3)
    "valueprop": ("Turning ambition into strategy, strategy into execution, "
                  "and execution into measurable performance."),
    "email": "info@thestrategist.com",
    "phone": "+20 100 000 0000",
    "whatsapp": "201000000000",
    "city": "Cairo, Egypt",
    "linkedin": "#",
    "markets": "Egypt, the GCC and the wider Middle East",
}

# ---------------------------------------------------------------- CLIENT copy
# Verbatim from "The Strategist Website v2" - do not reword without approval.

WHO_WE_ARE = [
    ("We are a management consulting firm helping organizations convert ambition into "
     "measurable business results. Our work integrates strategy, corporate performance, "
     "organization development, operating-model design and business transformation to "
     "address the full journey from direction to execution and sustainability."),
    ("We work through senior-level collaboration and cross-functional expertise, combining "
     "organizational insight with market realities to develop solutions that are practical, "
     "measurable and built for execution."),
]

VISION = ("To pioneer a new standard of strategic excellence across the GCC and MENA, where "
          "industries don't just participate in the economy but actively shape its future - "
          "with our firm recognized as the transformative partner making this possible and "
          "standing among the region's most influential consulting powerhouses.")

MISSION = ("We bridge the gap between vision and execution by transforming ambitious ideas "
           "into actionable strategies that deliver measurable, real-world business success.")

PHILOSOPHY = {
    "name": "The 4Ps Lens",
    "intro": ("We believe that strategy should be practical, people-driven, and built to win. "
              "Our approach centers on the 4Ps - People, Process, Product, and Profit - to "
              "assess organizational health and unlock potential. This lens ensures we see the "
              "full picture, not just the financials."),
    "items": [
        ("People", "Capability, structure, ownership and the behaviours that decide whether a plan survives contact with the organization."),
        ("Process", "How work actually flows - the operating discipline that turns intent into repeatable delivery."),
        ("Product", "The offer, the market it serves, and whether it still earns its place in the portfolio."),
        ("Profit", "The commercial outcome, tested against the cost and capital required to sustain it."),
    ],
}

METHODOLOGY = {
    "name": "Play to Win",
    "intro": ("Our \"Play to Win\" methodology brings together cross-functional experts from "
              "Finance, Commercial, HR, and Operations, alongside industry-specific specialists, "
              "to craft strategies that are both actionable and competitive. By combining internal "
              "insight with market realities, we help organizations define clear paths to "
              "sustainable success."),
}

APPROACH_INTRO = ("Our consulting lifecycle connects diagnosis to sustained results. Each engagement "
                  "is tailored to the client, while the six-stage lifecycle provides a disciplined "
                  "path from understanding the challenge to embedding performance.")

APPROACH = [
    ("Diagnose", "Understand the organization, current performance, challenges and root causes."),
    ("Define",   "Clarify strategic direction, priorities, desired outcomes and success criteria."),
    ("Design",   "Develop frameworks, operating models, KPIs, governance and solutions."),
    ("Execute",  "Translate recommendations into initiatives, ownership and implementation actions."),
    ("Measure",  "Track KPIs, initiatives, benefits and management performance."),
    ("Sustain",  "Embed governance, capabilities, continuous improvement and accountability."),
]

# ------------------------------------------------------------------- pillars

PILLARS = [
    {
        "slug": "strategy",
        "name": "Strategy",
        "blurb": "Clarity on direction, priorities and where to compete - translated into a plan the organization can actually execute.",
        "lede": ("Most organizations do not fail for lack of a strategy. They fail because the strategy "
                 "lives in a document rather than in the way the business is run. Our Strategy practice "
                 "builds direction that is specific enough to act on, and the management system that "
                 "keeps it alive after the offsite ends."),
        "icon": "target",
    },
    {
        "slug": "performance",
        "name": "Performance",
        "blurb": "Operating models, KPIs and governance that turn strategy into measurable, day-to-day performance.",
        "lede": ("A scorecard that nobody uses is a reporting exercise, not a performance system. Our "
                 "Performance practice builds the measures, the reporting rhythm and the review "
                 "discipline that change what management actually decides each month and each quarter."),
        "icon": "chart",
    },
    {
        "slug": "transformation",
        "name": "Transformation",
        "blurb": "Structured change programmes - from operating model to delivery - that make transformation stick.",
        "lede": ("Transformation stalls when ambition outruns governance. Our Transformation practice "
                 "designs how the organization should be structured and operate, then puts the roadmap, "
                 "the change agenda and the delivery system in place to get there."),
        "icon": "refresh",
    },
]

# --------------------------------------------------------------- 10 families
# name / value proposition / sub-service names are CLIENT (v2).
# challenges, whatwedo, capability descriptions, deliverables, outcomes are DRAFT.

FAMILIES = [
# ---------------------------------------------------------------- STRATEGY
{
    "slug": "strategic-management",
    "pillar": "strategy",
    "name": "Strategic Management",
    "valueprop": "Build a clear strategic direction and an execution system that turns priorities into accountable action.",
    "challenges": [
        ("The strategy exists as a document, not as a management system",
         "A plan was written, presented and filed. Nothing in the monthly operating rhythm changed as a result."),
        ("The leadership team is not aligned on what matters most",
         "Ask five executives for the top three priorities and you get eleven answers - each defensible, none shared."),
        ("Annual planning produces a budget, not a direction",
         "The process allocates money against last year's structure rather than against where the business intends to go."),
        ("Strategic initiatives lose their owner",
         "Initiatives are agreed at an offsite, then compete for attention with the day job and quietly stall."),
    ],
    "whatwedo": ("We work with executive teams to set a strategic direction that is specific enough to "
                 "be acted on, and then build the management system that keeps it in front of leadership "
                 "every month. That means a defensible strategy, a prioritized initiative portfolio with "
                 "named owners, a measurement set that reflects the strategy rather than the org chart, "
                 "and a Strategy Management Office with the mandate to hold the cycle together."),
    "capabilities": [
        ("Strategic Planning",
         "A structured planning cycle - environmental analysis, capability assessment, scenario framing and prioritization - that produces a plan the executive team owns rather than receives."),
        ("Strategy Formulation",
         "Defining where the organization will compete and how it will win: positioning, strategic choices, the objectives that follow from them, and the trade-offs leadership is agreeing to accept."),
        ("Strategy Execution",
         "Translating the plan into an initiative portfolio with charters, owners, sequencing, resourcing and dependencies - so execution has a structure instead of relying on goodwill."),
        ("Strategy Review",
         "A disciplined review cadence that tests whether assumptions still hold, whether initiatives are delivering, and what should be stopped, accelerated or re-scoped."),
        ("Strategy Management Office (SMO)",
         "Standing up the function that owns the strategic calendar, the reporting pack, initiative governance and the quality of strategic decision-making across the cycle."),
    ],
    "deliverables": [
        "Strategic plan and supporting analysis",
        "Strategy map linking objectives across perspectives",
        "Prioritized strategic initiative portfolio with charters and owners",
        "Strategic KPI set with baselines and targets",
        "SMO charter, operating calendar and governance model",
        "Quarterly strategy review pack and reporting template",
    ],
    "outcomes": [
        ("A leadership team that agrees on the same short list of priorities - and can say what they are not doing."),
        ("Strategic initiatives with named owners, defined scope and a governance forum that tracks them."),
        ("An annual cycle where planning, budgeting and performance review reference the same objectives."),
        ("Earlier warning when an assumption breaks, because review is built into the calendar rather than triggered by a crisis."),
    ],
},
{
    "slug": "business-advisory",
    "pillar": "strategy",
    "name": "Business Advisory",
    "valueprop": "Support critical growth and investment decisions with structured analysis and commercially grounded advice.",
    "challenges": [
        ("A major investment decision rests on advocacy rather than analysis",
         "The business case was built by the team that wants the outcome, and the downside has never been stress-tested."),
        ("Growth ambition has no evidence behind it",
         "Targets were set top-down. Nobody has sized the market, tested willingness to pay, or checked whether the capacity exists."),
        ("The business model still reflects an earlier era",
         "Margins are being defended by cost control because no one has revisited how the business actually creates and captures value."),
        ("Competitor moves are noticed late",
         "Market intelligence is anecdotal - collected by whoever happened to be at the conference."),
    ],
    "whatwedo": ("We bring structured commercial analysis to the decisions that carry the most risk: where "
                 "to grow, what to invest in, which markets to enter and which business models still earn "
                 "their place. Our work is deliberately evidence-led and deliberately independent of the "
                 "internal case being made - leadership gets a defensible basis for the decision, including "
                 "the scenarios in which the answer is no."),
    "capabilities": [
        ("Business Development",
         "Identifying, sizing and prioritizing commercial opportunities - new segments, channels, partnerships and offers - and building the plan to pursue them."),
        ("Growth Strategy",
         "Setting where growth will come from and in what sequence: organic expansion, adjacency, geography, acquisition or partnership, with the capability implications of each."),
        ("Business Model Assessment",
         "Testing how the organization creates, delivers and captures value - the revenue architecture, cost structure and margin logic - and where that model is under pressure."),
        ("Market Studies",
         "Structured demand-side research: market sizing, segmentation, customer needs, pricing dynamics and regulatory context in the target geography."),
        ("Competitive Analysis",
         "Mapping the competitive set, relative positioning, cost and capability comparison, and the moves most likely to change the basis of competition."),
        ("Feasibility Studies",
         "Full technical, commercial and financial feasibility with scenario modelling, sensitivity analysis and a clear recommendation on whether and how to proceed."),
    ],
    "deliverables": [
        "Market sizing and segmentation model",
        "Competitive landscape assessment and positioning map",
        "Business model and margin architecture review",
        "Growth options assessment with prioritization criteria",
        "Full feasibility study with financial model and sensitivities",
        "Investment recommendation and supporting decision pack",
    ],
    "outcomes": [
        "Investment and growth decisions supported by evidence rather than advocacy.",
        "A clear, sized view of where growth is available and what it will take to capture it.",
        "Early identification of business model pressure before it shows up in the margin.",
        "A defensible pack for board, investor or lender conversations.",
    ],
},
{
    "slug": "strategic-alignment",
    "pillar": "strategy",
    "name": "Strategic Alignment",
    "valueprop": "Connect strategic ambition with objectives, risks, opportunities, resources and organizational priorities.",
    "challenges": [
        ("Functional plans do not add up to the corporate strategy",
         "Each function has a credible plan. Together they do not deliver the stated ambition, and nobody has checked."),
        ("Risk management runs on a separate track from strategy",
         "The risk register catalogues operational exposure while the risks that could actually break the strategy go unowned."),
        ("Resources are committed to yesterday's priorities",
         "Budget and headcount follow historical allocation, not the objectives leadership says matter now."),
        ("Growth opportunities are assessed one at a time",
         "Each proposal is judged on its own merits, never against the others or against capacity to deliver."),
    ],
    "whatwedo": ("We test whether the organization is genuinely pointed in one direction - and make the "
                 "gaps visible. That means tracing the line from corporate ambition through functional "
                 "objectives to resource allocation, surfacing where the logic breaks, and assessing the "
                 "strategic risks and growth opportunities that sit outside any single function's remit."),
    "capabilities": [
        ("Strategy Maps",
         "A single-page causal model of how financial outcomes, customer results, internal processes and organizational capability connect - used to test whether the objectives actually reinforce one another."),
        ("Strategic Alignment Assessment",
         "A structured review of alignment between corporate strategy, functional plans, KPIs, budgets, structure and incentives - with the specific disconnects named."),
        ("Strategic Risk Assessment",
         "Identifying and assessing the risks that threaten strategic objectives rather than day-to-day operations, with ownership, appetite and mitigation built into governance."),
        ("Growth Opportunity Assessment",
         "Evaluating growth options against a consistent set of criteria - attractiveness, fit, capability, capital and risk - so the portfolio can be compared rather than argued."),
    ],
    "deliverables": [
        "Enterprise strategy map",
        "Alignment assessment with prioritized gap register",
        "Strategic risk register with owners and appetite statements",
        "Growth opportunity portfolio and scoring model",
        "Resource allocation review against stated priorities",
    ],
    "outcomes": [
        "Functional plans that visibly roll up to the corporate ambition.",
        "Strategic risks owned at the level where something can actually be done about them.",
        "Resource allocation that reflects current priorities rather than historical precedent.",
        "Growth options compared on a common basis instead of case by case.",
    ],
},
# ------------------------------------------------------------- PERFORMANCE
{
    "slug": "corporate-performance-management",
    "pillar": "performance",
    "name": "Corporate Performance Management",
    "valueprop": "Create an integrated system that translates strategy into measurable objectives, KPIs, targets and dashboards.",
    "challenges": [
        ("Hundreds of KPIs, none of them decisive",
         "Reporting has grown by accretion. Every measure has a champion and no measure changes a decision."),
        ("Targets are negotiated rather than derived",
         "Numbers are set by adding a percentage to last year, disconnected from the strategy they are meant to deliver."),
        ("Measures reflect the org chart, not the strategy",
         "Each function reports what it controls, so cross-functional outcomes - the ones the strategy depends on - go unmeasured."),
        ("Dashboards describe the past",
         "By the time the pack is circulated, the period is closed and the opportunity to intervene has gone."),
    ],
    "whatwedo": ("We build the measurement system that connects strategic intent to what management "
                 "actually reviews. That starts with a deliberately short KPI set derived from the "
                 "strategy, definitions rigorous enough to survive disagreement, targets with a stated "
                 "basis, and dashboards designed around the decisions they are meant to support rather "
                 "than around the data that happens to be available."),
    "capabilities": [
        ("Corporate Performance Management (CPM)",
         "Designing the end-to-end performance architecture - objectives, measures, targets, reporting and review - as one integrated system rather than separate initiatives."),
        ("KPI Framework & Development",
         "Building a disciplined measure set with formal definitions, formulas, data sources, owners, frequency and thresholds, so numbers mean the same thing in every forum."),
        ("Balanced Scorecard (BSC)",
         "Implementing the scorecard across financial, customer, process and learning perspectives, cascaded to the level where accountability genuinely sits."),
        ("OKRs",
         "Introducing objectives and key results where directional focus and shorter cycles matter more than exhaustive measurement - including how OKRs coexist with existing KPIs."),
        ("Performance Dashboards",
         "Designing management and executive dashboards around the decisions they support: leading indicators, variance, trend and drill-down, not a wall of gauges."),
    ],
    "deliverables": [
        "Corporate KPI framework with full definition catalogue",
        "Balanced scorecard, cascaded to business unit and function",
        "Target-setting methodology with documented basis",
        "OKR structure and cycle design where applicable",
        "Executive and management dashboard specifications",
        "Data source, ownership and refresh mapping",
    ],
    "outcomes": [
        "A short, defensible measure set that leadership actually uses.",
        "Consistent definitions - the same number means the same thing in every forum.",
        "Targets with a stated basis, so variance conversations are about causes rather than fairness.",
        "Dashboards that surface problems early enough to act on them.",
    ],
},
{
    "slug": "performance-governance",
    "pillar": "performance",
    "name": "Performance Governance",
    "valueprop": "Establish the management rhythm, reporting discipline and corrective-action mechanisms required for accountability.",
    "challenges": [
        ("Review meetings explain the past instead of deciding the future",
         "Two hours are spent walking through what happened. Nothing is decided, and nobody leaves with an action."),
        ("Red items stay red",
         "A measure goes off-track, is noted, and appears again next month in the same condition."),
        ("Reporting is an assembly exercise",
         "The pack takes a week to build, is contested when it lands, and is out of date on arrival."),
        ("Accountability is diffuse",
         "Everyone in the room is responsible for the number, which means nobody is."),
    ],
    "whatwedo": ("We build the management rhythm that turns measurement into accountability: who meets, "
                 "how often, on what evidence, and what is required to leave the room. The design covers "
                 "the meeting architecture from operational review to board, the standard of reporting "
                 "that supports it, and a corrective-action mechanism with enough teeth that an "
                 "off-track measure triggers a response rather than a note."),
    "capabilities": [
        ("Performance Review Framework",
         "Defining the full review architecture - forums, membership, frequency, decision rights and escalation paths - from operational review through to board oversight."),
        ("Performance Reporting",
         "Standardizing reporting content, format, calendar and data quality so packs are consistent, timely and trusted enough to be argued from rather than about."),
        ("Management Dashboards",
         "Building the working views each management layer needs, aligned to their decision rights, with drill-down to the level where the cause actually sits."),
        ("Management Review Meetings",
         "Redesigning the meeting itself - agenda, pre-read discipline, time allocation, exception focus and decision capture - so the forum produces decisions rather than commentary."),
        ("Corrective Action Framework",
         "Establishing what happens when a measure goes off-track: trigger thresholds, root-cause requirement, action ownership, timeline and follow-through at the next review."),
    ],
    "deliverables": [
        "Performance governance model and forum architecture",
        "Meeting calendar with membership and decision rights",
        "Standard reporting pack templates by level",
        "Management dashboard set aligned to decision rights",
        "Corrective action protocol with escalation thresholds",
        "Decision and action log discipline",
    ],
    "outcomes": [
        "Review meetings that end with owned decisions and dated actions.",
        "Off-track measures that trigger a documented response rather than a repeat appearance.",
        "Reporting that arrives on time and is trusted enough to argue from.",
        "Clear accountability at each management layer for a defined set of outcomes.",
    ],
},
{
    "slug": "strategic-portfolio-performance",
    "pillar": "performance",
    "name": "Strategic Portfolio Performance",
    "valueprop": "Improve visibility and control over strategic initiatives, portfolios, projects and realized benefits.",
    "challenges": [
        ("Nobody can say what the portfolio actually contains",
         "Initiatives were approved at different times through different routes. There is no single, current list."),
        ("Benefits are claimed at approval and never verified",
         "The business case justified the spend. No one returned to check whether the benefit arrived."),
        ("Delivery status is self-reported and optimistic",
         "Projects run green until shortly before they run red, because status reflects sentiment rather than evidence."),
        ("The PMO reports on projects but does not improve them",
         "It has become an administrative function collecting updates rather than a control function driving delivery."),
    ],
    "whatwedo": ("We give leadership a defensible view of what the organization is delivering, what it is "
                 "costing, and what it is actually returning. That means one consolidated portfolio, "
                 "evidence-based status, benefits tracked past approval into realization, and a PMO whose "
                 "own performance is measured on delivery outcomes rather than on reporting compliance."),
    "capabilities": [
        ("Strategic Initiative Tracking",
         "One consolidated register of strategic initiatives with scope, owner, milestones, dependencies, spend and evidence-based status - visible in a single view."),
        ("Portfolio Performance",
         "Assessing the portfolio as a whole: balance, capacity, strategic contribution, interdependency and the initiatives that should be stopped to protect the ones that matter."),
        ("Benefits Realization",
         "Defining benefits at approval with baselines and measurement method, then tracking them through delivery and into operations to confirm they were actually realized."),
        ("PMO Performance",
         "Reviewing the PMO's mandate, operating model and value contribution - and re-positioning it from administrative reporting to genuine delivery control."),
        ("Project Performance",
         "Establishing consistent project standards, health assessment, stage gates and intervention triggers, with independent assurance on the initiatives that carry most risk."),
    ],
    "deliverables": [
        "Consolidated strategic initiative portfolio register",
        "Portfolio dashboard with capacity and dependency view",
        "Benefits realization framework with baselines and tracking",
        "Stage-gate model and project health assessment standard",
        "PMO mandate, operating model and performance measures",
        "Portfolio governance and prioritization protocol",
    ],
    "outcomes": [
        "One current, trusted view of everything the organization is delivering.",
        "Benefits verified after delivery, not assumed at approval.",
        "Earlier and more honest escalation, because status rests on evidence.",
        "A PMO that improves delivery rather than documenting it.",
    ],
},
# ---------------------------------------------------------- TRANSFORMATION
{
    "slug": "organization-development",
    "pillar": "transformation",
    "name": "Organization Development",
    "valueprop": "Align structure, roles, governance and job architecture with the strategy and future operating requirements.",
    "challenges": [
        ("The structure reflects history rather than strategy",
         "Reporting lines were drawn around people and past acquisitions, and have never been revisited against where the business is going."),
        ("Job titles do not describe comparable work",
         "The same title carries different scope in different units, which makes pay, progression and workforce planning arbitrary."),
        ("Decision rights are unwritten",
         "Authority is understood informally, which works until it is contested - and then escalates."),
        ("Restructuring is announced before it is designed",
         "The new chart is published, and the operating detail is worked out afterwards, at cost."),
    ],
    "whatwedo": ("We design the organization the strategy requires - structure, roles, governance and "
                 "job architecture - and then design the path from the current state to it. The work is "
                 "deliberately detailed: an org chart is the easy part, and the value is in the "
                 "accountability, decision rights and role definition that sit underneath it."),
    "capabilities": [
        ("Organization Design",
         "Designing structure against strategic requirements - grouping logic, spans and layers, coordination mechanisms and the interfaces between units."),
        ("Organizational Restructuring",
         "Planning and sequencing the move from current to target structure, including transition design, role mapping, risk management and communication."),
        ("Job Architecture",
         "Building a consistent framework of job families, levels and role profiles so that scope, capability and progression are comparable across the organization."),
        ("Governance Framework",
         "Defining committee structure, mandates, membership, decision rights and reporting lines - the formal machinery through which the organization decides."),
        ("Roles & Responsibilities",
         "Documenting accountability at role level, resolving the overlaps and gaps that create duplicated effort and unowned work."),
    ],
    "deliverables": [
        "Target organization structure with design rationale",
        "Role profiles and accountability definitions",
        "Job architecture with families, levels and criteria",
        "Governance framework and committee charters",
        "Transition and implementation plan",
        "Spans, layers and structural cost analysis",
    ],
    "outcomes": [
        "A structure that follows from the strategy and can be explained in those terms.",
        "Comparable roles across units, giving pay and progression a defensible basis.",
        "Written decision rights, so authority is settled before it is contested.",
        "Restructuring executed to a plan rather than improvised after announcement.",
    ],
},
{
    "slug": "target-operating-model",
    "pillar": "transformation",
    "name": "Target Operating Model",
    "valueprop": "Design how the organization should operate across structure, decision rights, processes, governance and shared capabilities.",
    "challenges": [
        ("Strategy changed; the operating model did not",
         "New ambitions are being pursued through a way of working designed for a different business."),
        ("Corporate centre and business units duplicate each other",
         "Both build the same capability because the split of responsibility was never made explicit."),
        ("Approval chains are long and unclear",
         "Decisions travel further than they need to because authority limits are undocumented or out of date."),
        ("Shared services were set up to cut cost and now constrain the business",
         "The model was designed around consolidation rather than around the service the business needs."),
    ],
    "whatwedo": ("We design how the organization should work - not just how it should be drawn. A target "
                 "operating model covers the full set of design choices: what sits where, who decides "
                 "what, how the core processes run end to end, which capabilities are shared, and the "
                 "governance holding it together. We then define the path from today's model to the "
                 "target, in a sequence the organization can absorb."),
    "capabilities": [
        ("TOM Design",
         "Designing the target operating model across structure, process, governance, people, technology and information - as a coherent set of choices rather than isolated fixes."),
        ("RACI",
         "Mapping responsibility, accountability, consultation and information across end-to-end processes to eliminate duplicated work and unowned handoffs."),
        ("Authority Matrix",
         "Defining delegation of authority by decision type and value threshold, so approval routes are explicit, proportionate and auditable."),
        ("Policies & Procedures",
         "Developing the policy architecture and supporting procedures that make the operating model enforceable rather than aspirational."),
        ("Shared Services / COE Design",
         "Designing shared service and centre-of-excellence models - scope, service catalogue, service levels, governance and the retained organization around them."),
    ],
    "deliverables": [
        "Target operating model blueprint across all design dimensions",
        "End-to-end process ownership and RACI matrices",
        "Delegation of authority matrix",
        "Policy architecture and priority procedure set",
        "Shared services / COE design and service catalogue",
        "Operating model transition roadmap",
    ],
    "outcomes": [
        "An operating model that matches the strategy rather than the previous one.",
        "Clear separation of corporate and business unit responsibility, removing duplication.",
        "Decisions taken at the right level, with authority written down.",
        "Shared capabilities designed around service, not only around cost.",
    ],
},
{
    "slug": "process-operational-excellence",
    "pillar": "transformation",
    "name": "Process & Operational Excellence",
    "valueprop": "Simplify work, remove inefficiency and establish disciplined, scalable processes.",
    "challenges": [
        ("The documented process is not the real one",
         "Procedures exist, and the organization works around them, so improvement targets a process nobody follows."),
        ("Handoffs are where the time goes",
         "Individual steps are efficient. The waiting between them is not measured by anyone."),
        ("Growth has outpaced process discipline",
         "What worked at one site or one volume is breaking now, and the response has been to add headcount."),
        ("Improvement does not survive the project",
         "Gains are made during the initiative and erode once the team disbands, because nothing was embedded."),
    ],
    "whatwedo": ("We map how work actually flows, quantify where time and cost are genuinely lost, and "
                 "redesign the process around the outcome rather than the department. The emphasis "
                 "throughout is on what will still be running a year later: standard work that reflects "
                 "reality, ownership at process level rather than function level, and measures that make "
                 "drift visible before it becomes normal."),
    "capabilities": [
        ("Process Mapping",
         "Documenting end-to-end processes as they actually run - including handoffs, rework loops, wait states and the workarounds people have built."),
        ("Process Improvement",
         "Structured redesign using lean and root-cause methods to remove non-value-adding steps, reduce cycle time and eliminate the causes of rework."),
        ("Operational Excellence",
         "Establishing the management practices that sustain performance: standard work, visual management, tiered daily accountability and continuous improvement discipline."),
        ("Workflow Optimization",
         "Rebalancing work across roles, systems and handoff points to reduce queueing and remove bottlenecks - including where automation genuinely earns its place."),
        ("SOP Development",
         "Writing standard operating procedures that reflect the redesigned process and are usable at the front line, with review and version control built in."),
    ],
    "deliverables": [
        "End-to-end process maps of current and target state",
        "Process performance baseline: cycle time, cost, quality, rework",
        "Redesigned process flows with control points",
        "Standard operating procedure set",
        "Process ownership model and governance",
        "Continuous improvement operating rhythm",
    ],
    "outcomes": [
        "Measurable reduction in cycle time and rework on the processes that matter most.",
        "Procedures that reflect how the work is actually done, so they get used.",
        "Process ownership that survives functional boundaries.",
        "Improvement that persists after the project team leaves.",
    ],
},
{
    "slug": "business-transformation",
    "pillar": "transformation",
    "name": "Business Transformation",
    "valueprop": "Translate transformation ambition into a governed roadmap, change agenda and delivery system.",
    "challenges": [
        ("Transformation is a label attached to a list of projects",
         "Existing initiatives were relabelled. Nothing was re-sequenced, re-scoped or stopped."),
        ("The roadmap ignores the organization's capacity to absorb change",
         "Everything is scheduled to start now, competing for the same scarce people."),
        ("Change management means communication",
         "The programme has a comms plan and no serious answer to the behaviours that need to change."),
        ("Digital investment precedes the operating model",
         "Technology is being implemented on top of processes and structures that will not support it."),
    ],
    "whatwedo": ("We turn transformation ambition into something governable: a sequenced roadmap tested "
                 "against real capacity, a delivery system with the authority to make decisions at pace, "
                 "and a change agenda that addresses behaviour rather than announcements. Where "
                 "technology is central, we work on the operating model first, so digital investment "
                 "lands on a structure capable of using it."),
    "capabilities": [
        ("Business Transformation",
         "Framing the transformation - scope, ambition, value case, design principles and the sequence of change required to deliver it."),
        ("Change Management",
         "Structured change delivery: stakeholder analysis, impact assessment, capability building, resistance management and adoption measurement."),
        ("Digital Transformation Advisory",
         "Advising on digital ambition and sequencing from the business side - process and operating model readiness, value case, and the order in which technology should land."),
        ("Transformation Roadmap",
         "Sequencing initiatives against dependency, capacity and value, with clear phases, gates and the trade-offs made explicit."),
        ("Transformation Office / PMO",
         "Establishing the delivery function that governs the programme: mandate, decision rights, reporting, risk and issue escalation, and benefits oversight."),
    ],
    "deliverables": [
        "Transformation strategy and value case",
        "Phased transformation roadmap with dependencies and gates",
        "Transformation office charter and governance model",
        "Change impact assessment and adoption plan",
        "Capacity and readiness assessment",
        "Benefits framework and tracking model",
    ],
    "outcomes": [
        "A roadmap sequenced against what the organization can actually absorb.",
        "A transformation office with the authority to decide, not only to report.",
        "Change measured by adoption rather than by communications delivered.",
        "Digital investment landing on an operating model ready to use it.",
    ],
},
]

# ------------------------------------------------------------------ DRAFT
# Everything below is drafted for client review - tagged on the site.

INDUSTRIES = [
    ("Government & Public Sector",
     "National and local entities delivering reform agendas, service transformation and performance accountability against published targets."),
    ("Financial Services",
     "Banks, insurers and financial groups balancing regulatory demand, digital competition and cost-to-income pressure."),
    ("Energy, Utilities & Industrial",
     "Capital-intensive operators where asset performance, operating discipline and portfolio governance decide the margin."),
    ("Healthcare & Pharmaceuticals",
     "Providers and manufacturers managing clinical quality, regulatory obligation and operational throughput at the same time."),
    ("Real Estate & Construction",
     "Developers and contractors managing large project portfolios where benefits realization and delivery control are decisive."),
    ("Retail, FMCG & Consumer",
     "Businesses competing on route-to-market, channel economics and the speed of the commercial cycle."),
    ("Telecom, Technology & Media",
     "Organizations where operating models are being rebuilt around digital delivery and shorter planning horizons."),
    ("Family Businesses & Diversified Groups",
     "Groups formalizing governance, professionalizing management and separating ownership from executive control."),
]

CASE_STUDIES = [
    {
        "slug": "diversified-group-strategy-execution",
        "client": "Diversified industrial group",
        "anonymized": True,
        "sector": "Industrial / Family Group",
        "service": "Strategic Management",
        "service_slug": "strategic-management",
        "title": "Turning a five-year plan into a governed execution system",
        "excerpt": ("A family-owned group with six business units had an approved strategy that had not "
                    "changed how any unit was managed. We built the initiative portfolio, the measurement "
                    "set and the SMO that made it operational."),
        "challenge": ("The group had completed a five-year strategy the previous year. It had been approved by "
                      "the board and presented to management, but the operating rhythm was unchanged: each "
                      "business unit planned independently, capital was allocated on historical precedent, and "
                      "no forum existed to review strategic progress. Eighteen months in, leadership could not "
                      "say which parts of the strategy were on track."),
        "scope": ("A twelve-week engagement across the corporate centre and all six business units, covering "
                  "strategy translation, initiative portfolio definition, measurement design and the "
                  "establishment of a Strategy Management Office."),
        "approach": [
            "Reconstructed the strategy as a strategy map to expose objectives that had no owner or no measure.",
            "Consolidated every in-flight initiative across the group into a single register - identifying substantial duplication between units.",
            "Re-scoped the portfolio against strategic contribution and delivery capacity, stopping or deferring a material share of it.",
            "Designed a corporate KPI set with formal definitions and cascaded it to business unit scorecards.",
            "Stood up an SMO with a defined mandate, quarterly review calendar and standard reporting pack.",
        ],
        "deliverables": [
            "Group strategy map and objective ownership matrix",
            "Consolidated and re-prioritized initiative portfolio",
            "Corporate and business unit scorecards with definition catalogue",
            "SMO charter, calendar and governance model",
            "Quarterly strategic review pack template",
        ],
        "outcome": ("The group moved from an annual budget conversation to a quarterly strategic review with "
                    "named owners for every objective. Duplicate initiatives across business units were "
                    "consolidated, releasing delivery capacity back to the priorities the board had actually "
                    "approved."),
        "metrics": [
            ("6", "business units brought onto one portfolio view"),
            ("12", "weeks from mobilization to first governed review"),
            ("1", "consolidated initiative register replacing six"),
        ],
    },
    {
        "slug": "public-sector-performance-governance",
        "client": "National public-sector entity",
        "anonymized": True,
        "sector": "Government & Public Sector",
        "service": "Performance Governance",
        "service_slug": "performance-governance",
        "title": "Rebuilding a performance review cycle that produced decisions",
        "excerpt": ("A national entity reported against more than two hundred indicators each month without "
                    "the review cycle changing any management decision. We rebuilt the measure set, the "
                    "reporting standard and the meeting architecture around it."),
        "challenge": ("Monthly performance reporting had grown to over two hundred indicators compiled by a "
                      "central team. Preparing the pack consumed most of a week; the review meeting was spent "
                      "validating numbers rather than acting on them. Indicators that fell off-track were noted "
                      "and reappeared unchanged the following month."),
        "scope": ("A sixteen-week engagement covering measure rationalization, reporting standardization, "
                  "review forum redesign and the introduction of a corrective-action protocol."),
        "approach": [
            "Audited the full indicator set against strategic objectives and decision relevance, retiring measures that informed no decision.",
            "Rebuilt definitions for the retained measures, resolving inconsistencies between departments reporting the same metric differently.",
            "Redesigned the reporting pack around exception and trend rather than exhaustive listing.",
            "Restructured the review forum: pre-read discipline, exception-focused agenda, explicit decision capture.",
            "Introduced a corrective-action protocol with trigger thresholds, mandatory root-cause analysis and follow-through at the next review.",
        ],
        "deliverables": [
            "Rationalized KPI set with full definition catalogue",
            "Standard reporting pack template and production calendar",
            "Review forum architecture with membership and decision rights",
            "Corrective action protocol and escalation thresholds",
            "Decision and action log discipline",
        ],
        "outcome": ("Reporting effort fell substantially while the review meeting shifted from validation to "
                    "decision-making. Off-track indicators began triggering documented corrective actions with "
                    "named owners and review dates, rather than recurring unchanged."),
        "metrics": [
            ("200+", "indicators reduced to a decision-relevant core set"),
            ("16", "weeks to redesigned governance cycle"),
            ("100%", "of off-track measures carrying an owned corrective action"),
        ],
    },
    {
        "slug": "financial-services-operating-model",
        "client": "Regional financial group",
        "anonymized": True,
        "sector": "Financial Services",
        "service": "Target Operating Model",
        "service_slug": "target-operating-model",
        "title": "Separating corporate centre and business unit accountability",
        "excerpt": ("Duplicated capability between the corporate centre and three business units was adding "
                    "cost and slowing decisions. We designed the target operating model and the delegation "
                    "of authority underneath it."),
        "challenge": ("Following two acquisitions, the group had a corporate centre and three business units "
                      "building overlapping capability in risk, technology and marketing. Approval routes "
                      "differed by unit, authority thresholds were undocumented, and decisions that should have "
                      "been local were escalating to group."),
        "scope": ("An eighteen-week engagement covering operating model design, responsibility mapping, "
                  "delegation of authority and the transition plan."),
        "approach": [
            "Mapped current-state responsibility across group and business units to quantify duplication.",
            "Established design principles with the executive committee, including what would deliberately remain federated.",
            "Designed the target operating model across structure, process, governance and shared capability.",
            "Built end-to-end RACI matrices for the core cross-unit processes.",
            "Defined a delegation of authority matrix by decision type and value threshold.",
        ],
        "deliverables": [
            "Target operating model blueprint",
            "Corporate centre and business unit responsibility split",
            "End-to-end process RACI matrices",
            "Delegation of authority matrix",
            "Phased transition roadmap",
        ],
        "outcome": ("Overlapping capability was consolidated where scale justified it and deliberately left "
                    "federated where market responsiveness mattered more. Written authority thresholds shortened "
                    "approval routes for decisions that no longer needed to reach group."),
        "metrics": [
            ("3", "business units aligned to one operating model"),
            ("18", "weeks from mobilization to approved blueprint"),
            ("1", "delegation of authority matrix replacing informal practice"),
        ],
    },
]

INSIGHT_CATEGORIES = ["Articles", "Executive Insights", "Reports & Publications"]

INSIGHTS = [
    {
        "slug": "strategy-that-survives-the-offsite",
        "category": "Executive Insights",
        "title": "The strategy that survives the offsite",
        "date": "2026-08-18",
        "author": "The Strategist",
        "read": "6 min read",
        "service_slug": "strategic-management",
        "excerpt": ("Most strategies are not defeated by competitors. They are defeated by the calendar - "
                    "by an operating rhythm that never changed to accommodate them."),
        "body": [
            ("h2", "The document is not the strategy"),
            ("p", "Ask a management team whether they have a strategy and the answer is almost always yes. Ask what changed in the way the business is run once it was approved, and the conversation becomes noticeably shorter."),
            ("p", "This is the central failure mode we encounter. The analysis was sound, the choices were defensible, the board approved it. And then the organization returned to a management cycle - monthly operations review, quarterly forecast, annual budget - that makes no reference to any of it."),
            ("blockquote", "A strategy that does not appear in the operating calendar is a point of view, not a plan."),
            ("h2", "Three things that have to change"),
            ("p", "In our experience, strategy becomes real when three specific things change, and it stays theoretical when they do not."),
            ("h3", "1. The initiative portfolio becomes explicit"),
            ("p", "Every organization is already running initiatives. What most cannot produce is one current list of them, with owners, scope and strategic contribution. Until that register exists, the strategy is competing for resources against a set of commitments nobody can see."),
            ("h3", "2. Measurement follows the strategy, not the org chart"),
            ("p", "Functions report what they control. Strategy usually depends on outcomes that cut across functions - which means the outcomes that matter most are frequently the ones nobody is measuring. Fixing this is less about adding KPIs than about being willing to retire the ones that inform no decision."),
            ("h3", "3. A forum exists whose only job is strategic progress"),
            ("p", "Where strategic review is added to the end of an operational meeting, it is the item that gets cut when the agenda runs long. It needs its own forum, its own cadence and its own standard of evidence."),
            ("h2", "The uncomfortable part"),
            ("p", "Making these changes almost always means stopping something. Portfolios are over-committed relative to real delivery capacity, and adding strategic initiatives to an already saturated organization produces slower delivery across the board rather than faster progress on the priorities."),
            ("p", "The discipline is not in choosing what to pursue. It is in naming what will be stopped to make room for it."),
        ],
    },
    {
        "slug": "why-kpi-frameworks-fail",
        "category": "Articles",
        "title": "Why KPI frameworks fail, and what to build instead",
        "date": "2026-07-30",
        "author": "The Strategist",
        "read": "5 min read",
        "service_slug": "corporate-performance-management",
        "excerpt": ("Measurement systems rarely fail because the wrong metric was chosen. They fail because "
                    "nobody agreed what the number means or what happens when it moves."),
        "body": [
            ("h2", "More measures, less clarity"),
            ("p", "A common pattern: an organization concludes it is not managing performance well, so it builds a KPI framework. Two years later it has several hundred indicators, a reporting team, a monthly pack - and the same difficulty answering whether the business is on track."),
            ("p", "The instinct to add measurement is understandable and usually counterproductive. Indicators accumulate because each one has a sponsor and none has an expiry date."),
            ("h2", "Three failures, in order of frequency"),
            ("h3", "Definition drift"),
            ("p", "The same indicator is calculated differently by different units. Meetings are then spent reconciling numbers rather than acting on them. A formal definition catalogue - formula, source, owner, frequency, threshold - is unglamorous and resolves more disputes than any dashboard."),
            ("h3", "Targets without a basis"),
            ("p", "Where targets are negotiated rather than derived, variance discussions become arguments about fairness. When the basis is documented, the conversation moves to cause and response."),
            ("h3", "No consequence"),
            ("p", "The most common failure of all: an indicator goes red, is noted, and reappears red next month. Without a protocol defining what a threshold breach triggers - root cause, owner, action, review date - measurement is observation, not management."),
            ("blockquote", "A measure that changes no decision is a reporting cost, not a performance system."),
            ("h2", "What to build instead"),
            ("p", "Start from the decisions leadership needs to make, and work backwards to the smallest set of measures that informs them. A short, well-defined, consequential measure set will outperform a comprehensive one every time - not least because people will actually use it."),
        ],
    },
    {
        "slug": "operating-model-before-digital",
        "category": "Executive Insights",
        "title": "Fix the operating model before you buy the platform",
        "date": "2026-07-09",
        "author": "The Strategist",
        "read": "5 min read",
        "service_slug": "target-operating-model",
        "excerpt": ("Digital investment lands on whatever operating model already exists. If that model is "
                    "unclear, technology makes the confusion faster and more expensive."),
        "body": [
            ("h2", "A familiar sequence"),
            ("p", "A platform is selected, an integrator is appointed, a go-live date is set. Somewhere during design, the project discovers that the process it is automating differs by business unit, that ownership of the end-to-end flow is contested, and that approval thresholds exist only as convention."),
            ("p", "These are not technology problems. They are operating model questions that the technology programme has been asked to resolve under time pressure, by people without the authority to resolve them."),
            ("h2", "What should be settled first"),
            ("p", "Three things, none of which require a system to answer."),
            ("h3", "Who owns the end-to-end process"),
            ("p", "Not who owns each step - who owns the outcome across the whole flow, including the handoffs where most of the elapsed time is actually spent."),
            ("h3", "What the authority thresholds are"),
            ("p", "A workflow tool encodes approval routes. If the routes are undocumented, the configuration decision defaults to whoever is available during a design workshop."),
            ("h3", "Which variation is deliberate"),
            ("p", "Some process variation reflects genuine market or regulatory difference and should be preserved. Some is historical accident. Deciding which is which is a business judgement, and it is considerably cheaper to make before configuration than after."),
            ("blockquote", "Technology is very good at scaling whatever it is given. That includes ambiguity."),
            ("h2", "The practical implication"),
            ("p", "This is not an argument for delay. It is an argument for a short, well-scoped operating model workstream running ahead of - and then alongside - the technology programme, with the authority to make the decisions the programme will otherwise be forced to invent."),
        ],
    },
    {
        "slug": "pmo-that-improves-delivery",
        "category": "Articles",
        "title": "From reporting PMO to delivery control",
        "date": "2026-06-22",
        "author": "The Strategist",
        "read": "4 min read",
        "service_slug": "strategic-portfolio-performance",
        "excerpt": ("Most PMOs collect status. Fewer change outcomes. The difference is mandate, not method."),
        "body": [
            ("h2", "The administrative trap"),
            ("p", "A PMO is established to give leadership visibility. It builds templates, collects updates, produces a portfolio dashboard. Within a year it is regarded by project managers as an overhead and by executives as a source of numbers they do not fully trust."),
            ("p", "The cause is usually mandate. The PMO was given a reporting responsibility without a corresponding decision right, so it can describe a problem but cannot act on one."),
            ("h2", "What changes the equation"),
            ("ul", [
                "Evidence-based status, where a milestone is complete only against defined acceptance criteria - not sentiment.",
                "Stage gates with genuine authority to hold, re-scope or stop, exercised often enough to be credible.",
                "Benefits tracked past approval into realization, with the same rigour applied to the business case after delivery as before it.",
                "Capacity as a hard constraint on portfolio intake, rather than an observation made after commitments are already given.",
            ]),
            ("h2", "Measure the PMO on delivery"),
            ("p", "If the PMO's own measures are reporting compliance and template adoption, it will optimize for those. If they are forecast accuracy, benefits realized and the rate at which off-track initiatives are corrected, its behaviour changes accordingly."),
        ],
    },
]

LEADERSHIP = {
    "board": [
        {"name": "Board member name", "title": "Chair, Advisory Board",
         "bio": "Short biography, areas of expertise and LinkedIn link where approved. Profiles are added, ordered and activated by the firm.",
         "expertise": "Governance | Corporate strategy"},
        {"name": "Board member name", "title": "Advisory Board Member",
         "bio": "Short biography, areas of expertise and LinkedIn link where approved.",
         "expertise": "Financial services | Risk"},
        {"name": "Board member name", "title": "Advisory Board Member",
         "bio": "Short biography, areas of expertise and LinkedIn link where approved.",
         "expertise": "Public sector | Reform delivery"},
    ],
    "executives": [
        {"name": "Executive name", "title": "Managing Partner",
         "bio": "Title, biography, qualifications, sector experience, core capabilities and approved professional links.",
         "expertise": "Strategy | Performance"},
        {"name": "Executive name", "title": "Partner, Performance",
         "bio": "Title, biography, qualifications, sector experience, core capabilities and approved professional links.",
         "expertise": "CPM | Governance"},
        {"name": "Executive name", "title": "Partner, Transformation",
         "bio": "Title, biography, qualifications, sector experience, core capabilities and approved professional links.",
         "expertise": "Operating model | Change"},
    ],
    "experts": [
        {"name": "Expert name", "title": "Associate Expert", "expertise": "Balanced Scorecard | Public sector"},
        {"name": "Expert name", "title": "Associate Expert", "expertise": "Operating model | Financial services"},
        {"name": "Expert name", "title": "Associate Expert", "expertise": "Process excellence | Manufacturing"},
        {"name": "Expert name", "title": "Associate Expert", "expertise": "Organization design | Energy"},
        {"name": "Expert name", "title": "Associate Expert", "expertise": "PMO | Construction"},
        {"name": "Expert name", "title": "Associate Expert", "expertise": "Change management | Healthcare"},
    ],
}

PARTNER_CATEGORIES = ["Consulting alliance", "Technology provider", "Training partner", "Research & academic"]

PARTNERS = [
    ("Partner name", "Consulting alliance", "Short description of the partnership and the value it creates for clients."),
    ("Partner name", "Technology provider", "Short description of the partnership and the value it creates for clients."),
    ("Partner name", "Training partner", "Short description of the partnership and the value it creates for clients."),
    ("Partner name", "Research & academic", "Short description of the partnership and the value it creates for clients."),
]

CLIENTS = [
    ("Client name", "Government & Public Sector"),
    ("Client name", "Financial Services"),
    ("Client name", "Energy, Utilities & Industrial"),
    ("Client name", "Healthcare & Pharmaceuticals"),
    ("Client name", "Real Estate & Construction"),
    ("Client name", "Retail, FMCG & Consumer"),
    ("Client name", "Telecom, Technology & Media"),
    ("Client name", "Family Businesses & Diversified Groups"),
]

TESTIMONIALS = [
    {"quote": "Approved client quotation about the engagement, its delivery quality and its measurable impact. Testimonials are published only once approved and are not materially edited.",
     "name": "Client representative name", "title": "Chief Executive Officer", "org": "Organization name",
     "service": "Strategic Management", "featured": True},
    {"quote": "Approved client quotation about the engagement, its delivery quality and its measurable impact.",
     "name": "Client representative name", "title": "Chief Operating Officer", "org": "Organization name",
     "service": "Performance Governance", "featured": False},
    {"quote": "Approved client quotation about the engagement, its delivery quality and its measurable impact.",
     "name": "Client representative name", "title": "Head of Strategy", "org": "Organization name",
     "service": "Target Operating Model", "featured": False},
    {"quote": "Approved client quotation about the engagement, its delivery quality and its measurable impact.",
     "name": "Client representative name", "title": "Transformation Director", "org": "Organization name",
     "service": "Business Transformation", "featured": False},
]

WHY_US = [
    ("Integrated across the full journey",
     "Strategy, performance and transformation are one practice, not three. The team that sets the direction is accountable for the system that delivers it."),
    ("Senior-level engagement",
     "Work is led by senior practitioners working directly with the executive team, not delegated once the proposal is signed."),
    ("Built for execution",
     "Every deliverable is judged against whether the organization can operate it after we leave - not whether it presents well."),
    ("Cross-functional by design",
     "The Play to Win methodology brings Finance, Commercial, HR and Operations expertise into the same room as industry specialists."),
    ("Measurable by default",
     "Objectives, baselines and measurement method are defined at the start, so impact can be evidenced rather than asserted."),
    ("Regional depth",
     "Direct experience of how strategy, governance and performance actually work across Egypt, the GCC and the wider Middle East."),
]

CHALLENGES_HOME = [
    ("Strategic direction is unclear or contested at the top",
     "The executive team is not aligned on priorities, so resources are committed without conviction."),
    ("Performance systems do not drive real decisions",
     "KPIs and scorecards exist, but nothing in the management cycle changes when they move."),
    ("Transformation programmes stall before they deliver value",
     "Initiatives launch with momentum and lose it without ownership, governance or capacity."),
    ("The operating model no longer fits the strategy",
     "Structure, decision rights and processes were designed for a business the organization has outgrown."),
]
