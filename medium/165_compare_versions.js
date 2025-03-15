/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    let v1 = parseVersion(version1);
    let v2 = parseVersion(version2);
    
    // Pad the shorter version with zeros
    let maxLength = Math.max(v1.length, v2.length);
    while (v1.length < maxLength) v1.push(0);
    while (v2.length < maxLength) v2.push(0);
    
    // Compare corresponding revisions
    for (let i = 0; i < maxLength; i++) {
        if (v1[i] > v2[i]) return 1;
        if (v1[i] < v2[i]) return -1;
    }
    return 0;
};

var parseVersion = function (version) {
    return version.split(".").map(num => parseInt(num, 10));
};