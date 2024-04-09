def generate_popup(person):
    return f"""
    <div style="width: 300px;">
        <div style="margin: 10px 0; display: flex; align-items: center; gap: 10px;">
            <img style="border: 2px solid black; border-radius: 999px; object-fit: cover;" src="{person["image"]}" alt="{person["name"]}" width="40px" height="40px">
            <div>
                <h4 style="margin: 0; text-align: center;">{person["name"]}</h4>
                <a href="{person["wiki"]}">Уикипедияда оқу</a>
            </div>
        </div>
        <iframe style="border-radius: 4px;" width="100%" height="150" src="{person["youtube_url"]}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    """
