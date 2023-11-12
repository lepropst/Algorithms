function isValidDate(d) {
  return d instanceof Date && !isNaN(d);
}

function makeid(length) {
  let data_lexical = "";
  const data = [];
  data_tasks = [];
  const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  const nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  const charactersLength = characters.length;
  const numsLength = nums.length;
  let counter = 0;
  while (counter < length) {
    data_lexical += characters
      .charAt(Math.floor(Math.random() * charactersLength))
      .toUpperCase();
    data.push(nums[Math.floor(Math.random() * numsLength)]);
    let start = new Date(`05 October 2011, 1${counter - 1}:${counter - 1}`);
    let end = new Date(`05 October 2011, 1${counter}:30`);
    data_tasks.push({
      start: isValidDate(start) ? start.toISOString() : "",
      end: isValidDate(end) ? end.toISOString() : "",
    });
    counter += 1;
  }

  return { data, data_lexical, data_tasks };
}
const tmp = makeid(25);
console.log({ ...tmp, data: tmp.data.split("") });
