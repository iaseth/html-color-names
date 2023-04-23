import masterJson from '../master.json';

interface ColorJson {
	name: string,
	lowername: string,
	hex: string,
	palette: any
};

const palettes: any = {};
masterJson.colors.forEach((color: ColorJson) => {
	palettes[color.lowername] = color.palette
});

export default palettes;
