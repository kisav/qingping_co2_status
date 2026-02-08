from co2_detector import co2_status


async def check_status(bot):
    level_co2 = co2_status
    print(level_co2)
    if level_co2 >= 1000:
         await bot.send_message(f"У вас очень высокий уровень CO2! \n Целых {level_co2} ppm. \n Пора проветрить и потрогать траву!")

