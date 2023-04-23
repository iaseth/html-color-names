import masterJson from '../master.json';

interface PaletteType {
	"50": string,
	"100": string,
	"200": string,
	"300": string,
	"400": string,
	"500": string,
	"600": string,
	"700": string,
	"800": string,
	"900": string,
	"950": string
}

interface ColorJsonType {
	name: string,
	lowername: string,
	hex: string,
	palette: PaletteType
}

const colors: ColorJsonType[] = masterJson.colors;

export const palettes: any = {};
colors.forEach(color => {
	palettes[color.lowername] = color.palette
});

const hcn: any = {
	palettes
};

export default hcn;
