import asyncio


async def getProgram(state):

	async with state.proxy() as data:

	    for k,v in data["scoring"].items():
	        
	        if v["score"] >= data["max_score"]:
	            data["max_score"] = v["score"]
	            data["max_key"] = k

	    if len(data["scoring"][data["max_key"]]["programs"]) > 1:
	        data["programs"] = '\n-' + '\n-'.join([str(x) for  x in data["scoring"][data["max_key"]]["programs"]])
	    else:
	        data["programs"] = '\n-' + data["scoring"][data["max_key"]]["programs"][0]

	    data["floor"] = data["scoring"][data["max_key"]]["floor"]
	
	return data
