// 1) შექმენით მაპი რომელშიც იქნება 5 წყვილი თითოეულ წყვილში შეინახეთ key როგორც ჯგუფის დასახელება ხოლო მისი მნიშვნელობა
//  უნდა იყოს იმ ჯგუფის საუკეთესო მოსწავლის სახელი(თქვენ მოიფიქრეთ), დაბეჭდეთ ამ მაპის ზომა, და დაბეჭდეთ თითოეული ჯგუფის საუკეთესო მოსწავლის სახელი

const groupMap = new Map();

groupMap.set("group24", "ლუკა წულაია");
groupMap.set("group26", "გაბრიელ ჯობავა");
groupMap.set("group30", "ნიკოლოზ კობახიძე");
groupMap.set("group32", "დავით ხელაძე");
groupMap.set("group38", "კონსტანტინე პაპავა");

console.log(groupMap.size);

groupMap.forEach((student, group) => {
    console.log(`${group} ჯგუფის საუკეთესო მოსწავლე არის ${student}`);
});
