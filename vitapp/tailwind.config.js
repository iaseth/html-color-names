/** @type {import('tailwindcss').Config} */
export default {
	content: [
		"./src/**/*.{ts,tsx}"
	],
	theme: {
		extend: {
			transitionDelay: {
				'0': '0ms',
			}
		},
	},
	plugins: [
		function ({ addVariant }) {
			addVariant('ch', '& > *');
			addVariant('ch2', '& > * > *');
			addVariant('ch3', '& > * > * > *');
		}
	],
}

