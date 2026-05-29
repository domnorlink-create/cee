from fasthtml.common import *

# Initialize FastHTML application with an in-memory database configuration
app, rt = FastHTML(
    db_file=":memory:", 
    hdrs=(
        Script(src="https://cdn.tailwindcss.com"),
        Style("""
            @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Kantumruy+Pro:wght@300;400;500;600;700&display=swap');
            body {
                font-family: 'Kantumruy Pro', sans-serif;
                background-color: #020617;
            }
            .mono-data {
                font-family: 'JetBrains Mono', monospace;
            }
        """)
    )
)

@rt("/")
def get():
    # HEADER / NAVIGATION
    header = Header(
        Div(
            # Logo & Brand Alignment (Updated to DOWNLOAD CENTER)
            Div(
                Div(
                    Span("DC", cls="font-bold tracking-tighter text-slate-950 text-base mono-data"),
                    cls="h-10 w-10 rounded-xl bg-gradient-to-br from-yellow-400 via-amber-500 to-yellow-600 flex items-center justify-center shadow-lg shadow-yellow-500/10"
                ),
                Div(
                    Span("DOWNLOAD CENTER", cls="font-bold tracking-wider text-white text-base block leading-none"),
                    Span("ឯកសារយោងគណនេយ្យ និងឧបករណ៍ឌីជីថល", cls="text-[10px] text-slate-400 block mt-1"),
                ),
                cls="flex items-center gap-3"
            ),
            # Navigation Links
            Nav(
                A("អត្រាប្តូរប្រាក់", href="https://www.cambodiaexchange.today/", cls="hover:text-yellow-500 transition-colors"),
                A("ឯកសារយោងគណនេយ្យ", href="#", cls="hover:text-yellow-500 transition-colors"),
                A("ទាញយកកម្មវិធី", href="#", cls="text-yellow-500 font-medium border-b-2 border-yellow-500 pb-1"),
                A("ទាក់ទងយើង", href="https://www.cambodiaexchange.today/contact", cls="hover:text-yellow-500 transition-colors"),
                cls="hidden md:flex items-center gap-6 text-sm text-slate-300"
            ),
            # Language Switcher with Country Icon Layout
            Div(
                Div(
                    Svg(
                        Path(fill="#032ea1", d="M0 0h512v85.3H0zm0 255.7h512V341H0z"),
                        Path(fill="#e11d48", d="M0 85.3h512v170.4H0z"),
                        Path(fill="#fff", d="M256 109.1c-14.7 0-25.2 12-25.2 24.3V148H209c-12 0-20.2 11.2-16 23.6l10 30.1h106l10-30.1c4.2-12.4-4-23.6-16-23.6h-21.8v-14.6c0-12.3-10.5-24.3-25.2-24.3z"),
                        cls="w-4 h-3.5 rounded-sm object-cover", viewBox="0 0 512 341"
                    ),
                    Span("KH / KHR", cls="mono-data"),
                    cls="flex items-center gap-2 text-xs px-2.5 py-1 bg-slate-800 rounded border border-slate-700 text-slate-300 font-medium"
                ),
                cls="flex items-center gap-4"
            ),
            cls="mx-auto max-w-7xl px-6 py-4 flex items-center justify-between"
        ),
        cls="border-b border-slate-800 bg-slate-900/50 backdrop-blur sticky top-0 z-50"
    )

    # DOWNLOAD HERO HEADER
    hero_section = Section(
        Div(
            Span("v2026.1", cls="inline-flex items-center gap-1.5 rounded-full bg-yellow-500/10 px-3 py-1 text-xs font-medium text-yellow-500 border border-yellow-500/20 mb-4 font-mono"),
            H1("មជ្ឈមណ្ឌលទាញយកកម្មវិធីហិរញ្ញវត្ថុ", cls="text-3xl font-bold tracking-tight text-white sm:text-4xl"),
            P("បង្កើនល្បឿនការងារគ្រប់គ្រង និងគណនេយ្យរបស់អ្នកជាមួយកម្មវិធីជំនួយផ្លូវការ។ គណនាអត្រាប្តូរប្រាក់ ប្រកាសពន្ធ និងគ្រប់គ្រងទិន្នន័យបានលឿន និងមានសុវត្ថិភាពខ្ពស់។", cls="mt-4 mx-auto max-w-2xl text-sm text-slate-400 leading-relaxed"),
            cls="mx-auto max-w-7xl px-6 text-center"
        ),
        cls="relative overflow-hidden bg-gradient-to-b from-slate-900 to-slate-950 py-16 border-b border-slate-900"
    )

    # MAIN CONTENT BODY
    main_content = Main(
        Div(
            Button("Windows App", cls="bg-yellow-500 hover:bg-yellow-600 text-slate-950 font-semibold text-xs px-5 py-2.5 rounded-lg transition-all shadow-md shadow-yellow-500/10"),
            Button("Office Add-ins (Soon)", cls="bg-slate-900 opacity-60 cursor-not-allowed border border-slate-800 text-slate-400 text-xs px-5 py-2.5 rounded-lg"),
            Button("Developers (Soon)", cls="bg-slate-900 opacity-60 cursor-not-allowed border border-slate-800 text-slate-400 text-xs px-5 py-2.5 rounded-lg"),
            cls="flex justify-center gap-2 mb-12"
        ),
        
        Div(
            # Card 1: ACTIVE LIVE WINDOWS APP
            Div(
                Div(
                    Div(
                        Span("Desktop Client", cls="text-[11px] font-medium text-yellow-500 bg-yellow-500/10 px-2.5 py-1 rounded-md"),
                        Span("v1", cls="text-xs text-slate-500 mono-data"),
                        cls="flex items-center justify-between mb-4"
                    ),
                    H3("Cambodia Exchange Rate Tracker", cls="text-base font-bold text-white mb-2 group-hover:text-yellow-500 transition-colors"),
                    P("ទាញយកទិន្នន័យអត្រាប្តូរប្រាក់ប្រចាំថ្ងៃពីក្រសួងសេដ្ឋកិច្ច និងហិរញ្ញវត្ថុដោយស្វ័យប្រវត្តិ ចូលទៅក្នុងប្រព័ន្ធកុំព្យូទ័ររបស់អ្នកផ្ទាល់។", cls="text-xs text-slate-400 leading-relaxed mb-6"),
                    Div(
                        Div(Span("ទំហំកញ្ចប់ឯកសារ:"), Span("96.1 MB", cls="text-slate-300 mono-data"), cls="flex justify-between"),
                        Div(Span("តម្រូវការប្រព័ន្ធ:"), Span("Windows 10/11 (64-bit)", cls="text-slate-300"), cls="flex justify-between"),
                        cls="space-y-2 border-t border-slate-800 pt-4 text-xs text-slate-400 font-normal"
                    ),
                ),
                Div(
                    A("ទាញយកកម្មវិធីដំឡើង (.exe)", href="https://download.domnor.link/cambodia-excange-v1/Cambodia%20Exchange%20Today%20Setup%201.0.0.exe", cls="block text-center w-full bg-yellow-500 hover:bg-yellow-600 text-slate-950 font-bold text-xs py-3 rounded-xl shadow-lg shadow-yellow-500/5 transition-all"),
                    cls="mt-6"
                ),
                cls="rounded-2xl border border-slate-800 bg-slate-900 p-6 flex flex-col justify-between hover:border-yellow-500/30 transition-all group shadow-xl ring-1 ring-yellow-500/5"
            ),

            # Card 2: COMING SOON OFFICE ADD-IN
            Div(
                Div(Span("ជិតមកដល់ហើយ", cls="text-[10px] uppercase tracking-wider font-semibold text-amber-400 bg-amber-400/10 px-2 py-0.5 rounded"), cls="absolute top-3 right-3"),
                Div(
                    Div(
                        Span("Office Add-in", cls="text-[11px] font-medium text-slate-500 bg-slate-800 px-2.5 py-1 rounded-md"),
                        Span("v1.0.0", cls="text-xs text-slate-600 mono-data"),
                        cls="flex items-center justify-between mb-4"
                    ),
                    H3("Accounting & Tax Excel Add-in", cls="text-base font-bold text-slate-400 mb-2"),
                    P("កម្មវិធីជំនួយសម្រាប់ Microsoft Excel ដើម្បីសម្រួលការគណនាពន្ធ និងបំប្លែងប្រាក់រៀលទៅតាមច្បាប់គណនេយ្យកម្ពុជា។", cls="text-xs text-slate-400 leading-relaxed mb-6"),
                    Div(
                        Div(Span("ទំហំកញ្ចប់ឯកសារ:"), Span("-- MB", cls="text-slate-600 mono-data"), cls="flex justify-between"),
                        Div(Span("តម្រូវការប្រព័ន្ធ:"), Span("MS Excel 2019+ / Office 365", cls="text-slate-600"), cls="flex justify-between"),
                        cls="space-y-2 border-t border-slate-800/60 pt-4 text-xs text-slate-600 font-normal"
                    ),
                ),
                Div(
                    Button("មិនទាន់បើកឱ្យទាញយក", disabled=True, cls="block text-center w-full bg-slate-800 border border-slate-700/50 text-slate-500 font-medium text-xs py-3 rounded-xl cursor-not-allowed"),
                    cls="mt-6"
                ),
                cls="rounded-2xl border border-slate-800 bg-slate-900/40 p-6 flex flex-col justify-between opacity-75 shadow-xl relative overflow-hidden"
            ),

            # Card 3: COMING SOON DEVELOPER RESOURCE
            Div(
                Div(Span("ជិតមកដល់ហើយ", cls="text-[10px] uppercase tracking-wider font-semibold text-amber-400 bg-amber-400/10 px-2 py-0.5 rounded"), cls="absolute top-3 right-3"),
                Div(
                    Div(
                        Span("Developer Resource", cls="text-[11px] font-medium text-slate-500 bg-slate-800 px-2.5 py-1 rounded-md"),
                        Span("v3.0.2", cls="text-xs text-slate-600 mono-data"),
                        cls="flex items-center justify-between mb-4"
                    ),
                    H3("Offline KHR Exchange API Tool", cls="text-base font-bold text-slate-400 mb-2"),
                    P("ឧបករណ៍ដំណើរការក្នុង Local Server សម្រាប់អ្នកអភិវឌ្ឍន៍កម្មវិធី (Developers) ដើម្បីភ្ជាប់ទិន្នន័យអត្រាប្តូរប្រាក់ចូលក្នុងប្រព័ន្ធ ERP។", cls="text-xs text-slate-500 leading-relaxed mb-6"),
                    Div(
                        Div(Span("ទំហំកញ្ចប់ឯកសារ:"), Span("-- MB", cls="text-slate-600 mono-data"), cls="flex justify-between"),
                        Div(Span("តម្រូវការប្រព័ន្ធ:"), Span("Node.js / Docker Runtime", cls="text-slate-600"), cls="flex justify-between"),
                        cls="space-y-2 border-t border-slate-800/60 pt-4 text-xs text-slate-600 font-normal"
                    ),
                ),
                Div(
                    Button("មិនទាន់បើកឱ្យទាញយក", disabled=True, cls="block text-center w-full bg-slate-800 border border-slate-700/50 text-slate-500 font-medium text-xs py-3 rounded-xl cursor-not-allowed"),
                    cls="mt-6"
                ),
                cls="rounded-2xl border border-slate-800 bg-slate-900/40 p-6 flex flex-col justify-between opacity-75 shadow-xl relative overflow-hidden"
            ),
            cls="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3"
        ),
        cls="mx-auto max-w-7xl px-6 py-12 flex-grow w-full"
    )

    # FOOTER (Updated to DOWNLOAD CENTER)
    footer = Footer(
        Div(
            Div("© 2026 DOWNLOAD CENTER · រក្សាសិទ្ធិគ្រប់យ៉ាង។", cls="mono-data"),
            Div(
                A("ឯកជនភាព", href="https://www.cambodiaexchange.today/privacy", cls="hover:text-yellow-500 transition-colors"),
                A("លក្ខខណ្ឌប្រើប្រាស់", href="https://www.cambodiaexchange.today/terms", cls="hover:text-yellow-500 transition-colors"),
                A("សេចក្តីបដិសេធ", href="https://www.cambodiaexchange.today/disclaimer", cls="hover:text-yellow-500 transition-colors"),
                A("ទំនាក់ទំនង", href="https://www.cambodiaexchange.today/contact", cls="hover:text-yellow-500 transition-colors"),
                cls="flex flex-wrap items-center gap-6"
            ),
            cls="mx-auto flex max-w-7xl flex-col items-center justify-between gap-4 px-6 py-6 text-xs text-slate-500 md:flex-row"
        ),
        cls="border-t border-slate-900 bg-slate-900/40 w-full"
    )

    return Title("មជ្ឈមណ្ឌលទាញយកកម្មវិធី — DOWNLOAD CENTER"), Body(
        header, hero_section, main_content, footer,
        cls="text-slate-200 antialiased min-h-full flex flex-col"
    )

# Expose server application hooks directly for root-level deployment environments
app = app
application = app
handler = app

if __name__ == "__main__":
    serve()
