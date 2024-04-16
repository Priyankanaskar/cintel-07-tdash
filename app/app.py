import seaborn as sns
from faicons import icon_svg 
from shiny import reactive
from shiny.express import input, render, ui
import palmerpenguins 

df = palmerpenguins.load_penguins()

ui.page_opts(title="Priyanka's Penguin Dashboard ")
ui.input_date("date", "Date")
def value():
    return input.date()
  
   
# Original UI layout and style setup
ui.HTML(
    """
  <style>
  body {
    background-color: #ADD8E6;
    color: #333; 
    font-family: Arial-bold, gothic;
    font-size: 16px; 
    font-weight: normal; 
    font-style: bold; 
    text-decoration: none; 
    text-transform: none; 
    line-height: 1.5; 
    letter-spacing: normal;
  }
  /* Add border style to headers 
  h1, h2, h3, h4, h5, h6 {
    border-bottom: 2px solid #333;
    padding-bottom: 5px; 
    margin-bottom: 10px; 
  }
  </style>
"""
)

with ui.sidebar(title="Filter controls",style="background-color: #e0ffff"):
    ui.input_slider("mass", "Mass", 2000, 6000, 6000)
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )
    ui.hr()
    ui.h6("Links")
    ui.a(
        "GitHub Source",
        href="https://github.com/Priyankanaskar/cintel-07-tdash",
        target="_blank",
    )
    ui.a(
        "GitHub App",
        href="https://priyankanaskar.github.io/cintel-07-tdash/",
        target="_blank",
    )

    ui.a(
        "GitHub Issues",
        href="https://github.com/Priyankanaskar/cintel-07-tdash/issues",
        target="_blank",
    )

    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")

    ui.a(
        "Template: Basic Dashboard",
        href="https://shiny.posit.co/py/templates/dashboard/",
        target="_blank",
    )
    ui.a(
        "See also",
        href="https://priyankanaskar.github.io/cintel-07-tdash/",
        target="_blank",
    )

with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("earlybirds"),theme="bg-gradient-blue-red"):
        "Number of penguins"

        @render.text
        def count():
            return filtered_df().shape[0]

    with ui.value_box(showcase=icon_svg("ruler-horizontal"),theme="bg-gradient-blue-red"):
        "Average bill length"

        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"

    with ui.value_box(showcase=icon_svg("ruler-vertical"),theme="bg-gradient-blue-red"):
        "Average bill depth"

        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"


with ui.layout_columns():
    with ui.card(full_screen=True,):
        ui.card_header("Bill length and depth")

        @render.plot
        def length_depth():
            return sns.scatterplot(
                data=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                hue="species",
            )

    with ui.card(full_screen=True):
        ui.card_header("Penguin data ")

        @render.data_frame
        def summary_statistics():
            cols = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)

<<<<<<< HEAD
penguins = sns.load_dataset("penguins")
ui.input_select("x", "Variable:",
                choices=["bill_length_mm", "bill_depth_mm"])
ui.input_select("dist", "Distribution:", choices=["hist", "kde"])
ui.input_checkbox("rug", "Show rug marks", value = False)
@render.plot
def displot():
    sns.displot(
        data=penguins, hue="species", multiple="stack",
        x=input.x(), rug=input.rug(), kind=input.dist())

ui.hr()
ui.input_action_button("show", "Explore")
@reactive.effect
@reactive.event(input.show)
def show_important_message():
    m = ui.modal(  
        "If you want to explore More Plot Please https://shiny.posit.co/py/templates/",  
        easy_close=True,  
        footer=None,  
    )  
    ui.modal_show(m)

ui.hr()

ui.input_text("Text", "Project Created By Priyanka",)

@render.text(inline=True)  
def text():
    return input.Text()
=======
# Card view for visualization---------------------------------------------------------------------------------------------------------------------------------------------------------

from shiny import App, ui

app_ui = ui.page_fillable(
    ui.layout_column_wrap(  
        ui.card("Card 1"),
        ui.card("Card 2"),
        ui.card("Card 3"),
        ui.card("Card 4"),
       width="2px",
        length="2px"
    ),
)
>>>>>>> bb8f96a3831050c9fddf11a3f8c4ce5d48bb5096

#ui.include_css(app_dir / "styles.css")


@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df
