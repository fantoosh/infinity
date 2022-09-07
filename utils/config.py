import discord


class Embeds:
    def __init__(self, title, description, color=discord.Colour.blurple()):
        self.embed_title = title
        self.embed_description = description
        self.embed_color = color
        self.embed = discord.Embed(title=self.embed_title, description=self.embed_description, color=self.embed_color)

    def create(self):
        self.embed.set_author(name="Charles", icon_url="https://drive.google.com/file/d/1dL0XsOGngmzj3a29YaFvZGHR8op666cX/view?usp=sharing")
        self.embed.set_thumbnail(url="https://example.com/link-to-my-thumbnail.png")
        self.embed.set_footer(text="Footer! No markdown here.")

    def add_field(self, *, name, value, inline=True):
        self.embed.add_field(name=name, value=value, inline=inline)

    def to_dict(self):
        return self.embed

