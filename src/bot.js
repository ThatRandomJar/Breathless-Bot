require("dotenv").config();

const { Client, Message } = require("discord.js");
const client = new Client();

const PREFIX = ".";

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', (msg) => {
  if (msg.author.bot) return;
    if (msg.content === 'UwU') {
      msg.channel.send('OwO');
    }

});

client.login(process.env.DISCORDJS_BOT_TOKEN);
