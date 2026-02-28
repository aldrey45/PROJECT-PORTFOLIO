from django.core.management.base import BaseCommand
from django.db import transaction

from portfolio.models import Profile, SnapshotItem
from projects.models import Project, ProjectHighlight, ProjectSection
from timeline.models import TimelineItem
from certifications.models import Certification


class Command(BaseCommand):
    help = "Seed the database with initial portfolio content."

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Seeding portfolio data..."))

        # --- Profile (single row) ---
        profile, _ = Profile.objects.get_or_create(
            name="Aldrey Pabilona",
            defaults={
                "headline": "Junior Full-Stack Developer (Backend-focused) | BSIT",
                "tagline": "I build system-driven web apps with REST APIs, RBAC, and production-style architecture.",
                "location": "Philippines",
                "email": "",
                "github_url": "https://github.com/aldrey45",
                "linkedin_url": "https://www.linkedin.com/in/aldrey-pabilona-34181a29b",
                "resume_url": "https://drive.google.com/file/d/1AaK8gMfRsWE4rdMWVqOwpvIgZJuhkU1k/view?usp=sharing",
            },
        )

        SnapshotItem.objects.filter(profile=profile).delete()
        snapshots = [
            ("Backend-heavy Full-Stack", "Laravel + Django + REST APIs", 1),
            ("REST API Design", "Clean endpoints + structured responses", 2),
            ("Docker + PostgreSQL", "Production-style local setup", 3),
            ("RBAC / Security mindset", "Roles, permissions, controlled access", 4),
        ]
        SnapshotItem.objects.bulk_create(
            [SnapshotItem(profile=profile, title=t, subtitle=s, order=o) for t, s, o in snapshots]
        )

        # --- Projects ---
        def upsert_project(data):
            project, _ = Project.objects.update_or_create(
                slug=data["slug"],
                defaults={k: v for k, v in data.items() if k not in ["highlights", "sections"]},
            )
            ProjectHighlight.objects.filter(project=project).delete()
            ProjectSection.objects.filter(project=project).delete()

            ProjectHighlight.objects.bulk_create(
                [ProjectHighlight(project=project, text=text, order=i + 1) for i, text in enumerate(data["highlights"])]
            )

            ProjectSection.objects.bulk_create(
                [
                    ProjectSection(project=project, title=sec["title"], content=sec["content"], order=sec["order"])
                    for sec in data["sections"]
                ]
            )
            return project

        capstone = {
            "title": "Logic-Based Code Similarity Detection System",
            "slug": "logic-based-code-similarity-detection",
            "one_liner": "Detects potential plagiarism by analyzing code sequence and structure—not just text similarity.",
            "overview": (
                "A system designed to identify potential plagiarism in programming activities by comparing logical flow and structure. "
                "It highlights matched blocks and produces similarity scores and reports for instructor review."
            ),
            "role": "Full-Stack",
            "year": "2025",
            "is_featured": True,
            "tech_stack": ["Laravel", "FastAPI", "PostgreSQL", "Redis", "Vue", "TypeScript", "Docker", "Piston API"],
            "tags": ["featured", "backend", "full-stack", "microservices", "api", "security"],
            "repo_url": "",
            "demo_url": "",
            "highlights": [
                "Built REST APIs for courses, activities, submissions, and detection results using Laravel.",
                "Integrated a Python FastAPI microservice for logic-based code similarity analysis.",
                "Developed instructor dashboard with similarity scoring, matched block highlighting, and reports.",
            ],
            "sections": [
                {
                    "title": "Architecture",
                    "content": (
                        "- Laravel web app for course/activity management and instructor dashboard\n"
                        "- FastAPI detector service for code similarity analysis\n"
                        "- PostgreSQL for data storage\n"
                        "- Redis for background processing/queue (optional)\n"
                        "- Piston API for sandboxed code execution"
                    ),
                    "order": 1,
                },
                {
                    "title": "Detection Method",
                    "content": (
                        "- Preprocessing/normalization to reduce formatting noise\n"
                        "- Sequence similarity compares token/line order to detect similar flow\n"
                        "- Structural similarity compares overall representation to catch paraphrased solutions\n"
                        "- Matched-block extraction + highlighting\n"
                        "- Final similarity score + explanation output"
                    ),
                    "order": 2,
                },
                {"title": "Challenges", "content": "- Handling different coding styles while keeping logic comparison fair.", "order": 3},
                {"title": "Results", "content": "- Produces similarity score, highlighted matches, and instructor-readable reports.", "order": 4},
            ],
        }

        visitor = {
            "title": "Visitor Management System",
            "slug": "visitor-management-system",
            "one_liner": "A web application for managing visitor booking and record tracking.",
            "overview": "A CRUD-based visitor management web app with booking and record management features.",
            "role": "Full-Stack",
            "year": "2024",
            "is_featured": False,
            "tech_stack": ["PHP", "MySQL", "HTML", "CSS", "Bootstrap"],
            "tags": ["web", "crud", "php"],
            "repo_url": "",
            "demo_url": "",
            "highlights": [
                "Implemented full CRUD operations for visitor booking and record management.",
                "Developed responsive UI using HTML, CSS, Bootstrap, and PHP with MySQL.",
                "Built dynamic forms and admin workflows for maintaining visitor data.",
            ],
            "sections": [
                {"title": "Overview", "content": "Focused on building a reliable CRUD workflow with a simple UI.", "order": 1},
            ],
        }

        recipe = {
            "title": "Recipe Mobile Application",
            "slug": "recipe-mobile-application",
            "one_liner": "Android recipe app with guided tutorials and Firebase authentication.",
            "overview": "A Kotlin-based Android app with Firebase Authentication and recipe tutorial flow.",
            "role": "Frontend",
            "year": "2024",
            "is_featured": False,
            "tech_stack": ["Kotlin", "Firebase Authentication", "Firebase"],
            "tags": ["mobile", "android", "firebase"],
            "repo_url": "",
            "demo_url": "",
            "highlights": [
                "Implemented Firebase Authentication (sign-up, sign-in, email verification, password reset).",
                "Integrated Firebase backend services for user data and account management.",
                "Developed Android recipe application using Kotlin with interactive recipe tutorials.",
            ],
            "sections": [
                {"title": "Overview", "content": "Designed a simple tutorial-driven cooking experience with user accounts.", "order": 1},
            ],
        }

        upsert_project(capstone)
        upsert_project(visitor)
        upsert_project(recipe)

        # --- Timeline ---
        TimelineItem.objects.all().delete()
        TimelineItem.objects.bulk_create(
            [
                TimelineItem(title="Started Capstone Development", type="capstone", description="Began building the code similarity detection system.", order=1),
                TimelineItem(title="OJT Experience (Backend Development)", type="ojt", description="Gained real-world backend development experience in an IT environment.", order=2),
                TimelineItem(title="Capstone Defense / Finalization", type="capstone", description="Finalized and defended the capstone project with improvements.", order=3),
                TimelineItem(title="Built Portfolio Backend (Django + Docker Postgres)", type="project", description="Created a public REST API for the portfolio with production-like setup.", order=4),
            ]
        )

        # --- Certifications (edit later with your real certs) ---
        Certification.objects.all().delete()
        Certification.objects.bulk_create(
            [
                Certification(title="(Add your certification)", issuer="Oracle / etc.", year="2025", credential_url="", badge_url=""),
            ]
        )

        self.stdout.write(self.style.SUCCESS("Seed complete"))