import discord


class Embeds:
    def __init__(self, title, description, color=discord.Colour.blurple()):
        self.embed_title = title
        self.embed_description = description
        self.embed_color = color
        self.embed = discord.Embed(title=self.embed_title, description=self.embed_description, color=self.embed_color)

    def create(self):
        self.embed.set_author(name="Charles", icon_url="https://example.com/link-to-my-image.png")
        self.embed.set_thumbnail(url="https://example.com/link-to-my-thumbnail.png")
        self.embed.set_footer(text="Footer! No markdown here.")
        self.embed.set_image(url="https://example.com/link-to-my-banner.png")

    def add_field(self, *, name, value, inline=True):
        self.embed.add_field(name=name, value=value, inline=inline)

    def to_dict(self):
        return self.embed

