const Discord = require("discord.js");
const client = new Discord.Client();

const config = require('./config.json')
const command = require('./commands')

client.on('ready', () =>
{ 
  console.log('The client is ready!')

  command(client, 'ping', msg => {
    msg.channel .send('Pong!')
  })
})

client.login(process.env.DISCORDJS_BOT_TOKEN
  );
