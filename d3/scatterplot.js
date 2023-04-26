const width = 800;
const height = 800;
const margin = { top: 20, right: 20, bottom: 20, left: 20 };

const svg = d3
  .select("body")
  .append("svg")
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", `${-width / 2} ${-height / 2} ${width} ${height}`);

const numRedPoints = 50;
const numBluePoints = 50;
const redRadius = 100;
const blueRadius = 200;

function generatePoints(numPoints, radius, color) {
  const points = [];
  for (let i = 0; i < numPoints; i++) {
    const angle = Math.random() * 2 * Math.PI;
    const r = Math.random() * radius;
    const x = r * Math.cos(angle);
    const y = r * Math.sin(angle);
    points.push({ x, y, color });
  }
  return points;
}

const redPoints = generatePoints(numRedPoints, redRadius, "red");
const bluePoints = generatePoints(numBluePoints, blueRadius, "blue");
const allPoints = redPoints.concat(bluePoints);

svg
  .selectAll("circle")
  .data(allPoints)
  .join("circle")
  .attr("cx", (d) => d.x)
  .attr("cy", (d) => d.y)
  .attr("r", 5)
  .attr("fill", (d) => d.color);
