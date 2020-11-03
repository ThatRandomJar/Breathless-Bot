const {prefix} = require('./config.json')

module.exports = (client, aliases, callback) => 
{
    client.on('message', (msg) => {
        if (typeof aliases === 'string'){
            aliases = [aliases]
        }
        const {content} = msg

        aliases.forEach(alias => {
            const command = `${prefix}${alias}`

            if (content.startsWith(`${command}`) || content === command)
            console.log(`Running the command ${command}`)
            callback(msg)
        });
    
    });
}